# -*- coding: utf-8 -*-
# spielstat main
#
# @author: nachos
# github.com/imnachos/spielstat

import logging
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.utils.project import get_project_settings
from spielstat.items import SpielstatItem
import json

class SpielstatSpider(scrapy.Spider):

    print('Starting Spielstat.')
    
    name = 'spielstat'
    
    def start_requests(self):
        print('Start scraping.')
        urls = ['http://www.marcadores.com/futbol/alemania/bundesliga/monchengladbach-stuttgart-m10541075.html']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
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
        self.logger.info('Home possession: %s ', item['homePossession'])
        stats.append(item['homePossession'])
        
        item['awayPossession'] = main_stats.xpath('//div[@class="away"]/span/text()')[0].extract()
        self.logger.info('Away possession: %s ', item['awayPossession'])
        stats.append(item['awayPossession'])
        
        stats_table = response.xpath('//div[@class="box-content ab-content"]/table')
        
        for s in stats_table.xpath('.//td[@class="stat-value"]/text()'):  
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
        
        outputTable.append(item['homeTeam']  + ' | ' +  item['scoreboard'] + ' | ' + item['awayTeam'] + ' \n')
        outputTable.append('---|---|---- \n')
        
        for s in range(len(stats)):

            if(s>1 and s%2 == 0):
                outputTable.append(stats[s] + ' | ' +  labels[int((s/2)-1)] + ' | ' + stats[s+1]  + ' \n')
                 
        self.logger.info('outputTable %s ', outputTable)
        item['statTable'] = outputTable
        
        yield item
        
