# -*- coding: utf-8 -*-
# spielstat main
#
# @author: nachos
# github.com/imnachos/spielstat

import logging
import scrapy
import praw
from scrapy.spiders import CrawlSpider
from scrapy.utils.project import get_project_settings
from spielstat.items import SpielstatItem
import json

class SpielstatSpider(scrapy.Spider):

    name = 'spielstat'
    reddit = praw.Reddit('spielstat')
    subreddit = reddit.subreddit("borussiadortmund")
    
    def start_requests(self):
        urls = ['http://www.marcadores.com/futbol/alemania/bundesliga/monchengladbach-stuttgart-m10541075.html']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
	
    def parse(self, response):
        item = SpielstatItem()
        stats = []
        outputTable = []
        labels = ['Possesion','Shots on goal', 'Missed shots', 'Corners', 'Offsides', 'Throw-ins', 'Infractions']
        
        self.logger.info('Parse called on: %s', response.url)
        #self.logger.info('Response body: %s', response.body)
        
        participantsData = response.xpath('//tr[@class="match-summary-teams"]')
         
        for p in participantsData.xpath('.//td[@class="participant-name"]/a/text()'):  
            stats.append(p.extract())
        
        item['homeTeam'] = stats[0]
        self.logger.info('Home team: %s ', item['homeTeam'])
        
        item['awayTeam'] = stats[1]
        self.logger.info('Away team: %s ', item['awayTeam'])
        
        item['homeGoals'] = participantsData.xpath('//td[@class="participant-score participant-score-home participant-score-runningscore-home"]/text()')[0].extract()
        self.logger.info('Home goals: %s ', item['homeGoals'])
        
        item['awayGoals'] = participantsData.xpath('//td[@class="participant-score participant-score-away participant-score-runningscore-away"]/text()')[0].extract()
        self.logger.info('Away goals: %s ', item['awayGoals'])
        
        item['scoreboard'] = item['homeGoals'] + '-' + item['awayGoals']
        
        main_stats = response.xpath('//div[@class="main-stats"]')
        
        item['homePossession'] = main_stats.xpath('//div[@class="home"]/span/text()')[0].extract()
        stats.append(item['homePossession'])
        self.logger.info('Home possession: %s ', item['homePossession'])
        
        item['awayPossession'] = main_stats.xpath('//div[@class="away"]/span/text()')[0].extract()
        stats.append(item['awayPossession'])
        self.logger.info('Away possession: %s ', item['awayPossession'])
        
        stats_table = response.xpath('//div[@class="box-content ab-content"]/table')
        
        for s in stats_table.xpath('.//td[@class="stat-value"]/text()'):  
            self.logger.info('Stat: %s ', s.extract())
            stats.append(s.extract())
        
        item['homeShotsOnGoal'] = stats[4]
        item['awayShotsOnGoal'] = stats[5]
        
        item['homeMissedShots'] = stats[6]
        item['awayMissedShots'] = stats[7]
        
        item['homeCorners'] = stats[8]
        item['awayCorners'] = stats[9]
        
        item['homeOffsides'] = stats[10]
        item['awayOffsides'] = stats[11]
        
        item['homeThrowIn'] = stats[12]
        item['awayThrowIn'] = stats[13]
        
        item['homeInfractions'] = stats[14]
        item['awayInfractions'] = stats[15]
        
        for s in range(len(stats)):
            self.logger.info('Array value: %s ', stats[s])
            if(s == 2):
                outputTable.append(stats[0] + ' | ' +  item['scoreboard'] + '  | ' + stats[1]  + ' \n ')
                outputTable.append('---|---|---- \n')
            elif(s > 2 and s %2 == 0):
                outputTable.append(stats[s-1] + ' | ' +  labels[s-4] + '  | ' + stats[s]  + ' \n ')
                 
        self.logger.info('outputTable %s ', outputTable)
        
