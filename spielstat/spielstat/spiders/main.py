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
        participants = []
        
        self.logger.info('Parse called on: %s', response.url)
        #self.logger.info('Response body: %s', response.body)
        
        participantsData = response.xpath('//tr[@class="match-summary-teams"]')
         
        for p in participantsData.xpath('.//td[@class="participant-name"]/a/text()'):  
            participants.append(p.extract())
        
        item['homeTeam'] = participants[0]
        self.logger.info('Home team: %s ', item['homeTeam'])
        
        item['awayTeam'] = participants[1]
        self.logger.info('Away team: %s ', item['awayTeam'])
        
        item['homeGoals'] = participantsData.xpath('//td[@class="participant-score participant-score-home participant-score-runningscore-home"]/text()').extract()
        self.logger.info('Home goals: %s ', item['homeGoals'])
        
        item['awayGoals'] = participantsData.xpath('//td[@class="participant-score participant-score-away participant-score-runningscore-away"]/text()').extract()
        self.logger.info('Away goals: %s ', item['awayGoals'])
        
        main_stats = response.xpath('//div[@class="main-stats"]')
        
        item['homePossession'] = main_stats.xpath('//div[@class="home"]/span/text()').extract()
        self.logger.info('Home possession: %s ', item['homePossession'])
            
        item['awayPossession'] = main_stats.xpath('//div[@class="away"]/span/text()').extract()
        self.logger.info('Away possession: %s ', item['awayPossession'])
        
        stats_table = response.xpath('//div[@class="box-content ab-content"]/table')
        
        for s in stats_table.xpath('.//td[@class="stat-value"]/text()'):  
            self.logger.info('Stat: %s ', s.extract())
            stats.append(s.extract())
        
        item['homeShotsOnGoal'] = stats[0]
        item['awayShotsOnGoal'] = stats[1]
        
        item['homeMissedShots'] = stats[2]
        item['awayMissedShots'] = stats[3]
        
        item['homeCorners'] = stats[4]
        item['awayCorners'] = stats[5]
        
        item['homeOffsides'] = stats[6]
        item['awayOffsides'] = stats[7]
        
        item['homeThrowIn'] = stats[8]
        item['awayThrowIn'] = stats[9]
        
        item['homeInfractions'] = stats[10]
        item['awayInfractions'] = stats[11]
        
        returnTable = 'Foo | Bar | text \n ' +' ---|---|---- \n ' +'Foo | Bar | text \n ' +'text | text | text \n ' +'text | text | text \n ' +'text | text | text \n ' +'text | text | text \n ' +'text | text | text'
        self.logger.info('returnTable %s ', returnTable)
        