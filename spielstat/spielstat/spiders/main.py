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

class SpielstatSpider(CrawlSpider):

    print('Starting Spielstat.')
    
    name = 'spielstat'
   
    def start_requests(self):
        print('Start scraping.')
        url = self.settings['TEAM_TO_SCRAPE']
        
        if(self.settings['SCRAPE_LEAGUES']):
            self.logger.info('Scrape leagues.')
            
            for league in self.settings['LEAGUES_TO_SCRAPE']:
                yield scrapy.Request(url=league, callback=self.getLiveMatches, encoding='utf-8')
        
        else:
            return scrapy.Request(url=url, callback=self.getLiveMatches, encoding='utf-8')
	   
    """
        Looks for a live game in a page
    """ 
    def getLiveMatches(self, response):  
        self.logger.info('Get live matches on: %s', response.url)
        #self.logger.info('Response body: %s', response.body)
        
        liveUrl = ''
        matchesTable = response.xpath('//tbody')

                 
        for liveRow in matchesTable.xpath('.//td[@class="event-status event-status-elapsed event-status-elapsed-ticking"]'):
            self.logger.info('liveRow: %s', liveRow)
            parentTable = liveRow.xpath('./..')
            self.logger.info('parentTable: %s', parentTable)
                               
            for liveMatch in parentTable.xpath('.//*[contains(@class, "event-score-col-runningscore event-score-runningscore")]'):
                gameLink = liveMatch.xpath('a[@class="lnk"]')
                liveUrl = 'http://www.marcadores.com' + gameLink.xpath('@href')[0].extract()
                self.logger.info('liveUrl: %s', liveUrl)
                yield scrapy.Request(url=liveUrl, callback=self.parseLiveMatch, encoding='utf-8')
        
    
    """
        Parses a match site
    """ 
    def parseLiveMatch(self, response):
        self.logger.info('Parse live match called on: %s', response.url)
        #self.logger.info('Response body: %s', response.body)

        item = SpielstatItem()
        stats = []
        siteLabels = []
        outputTable = []
        translations = {'Tiros a puerta' : 'Shots on goal', 'Tiros fuera' : 'Missed shots', 'Saques de falta' : 'Free kicks', 'Cรณrners' : 'Corners', 'Fueras de juego' : 'Offsides', 'Saques de banda' : 'Throw-ins', 'Paradas del portero' : 'Saves', 'Saques de centro' : 'Goal kicks', 'Faltas' : 'Infractions'}
         
        participantsData = response.xpath('//tr[@class="match-summary-teams"]')
         
        statusData = response.xpath('//tr[@class="match-summary-update"]')
        
        item['updateTime'] = statusData.xpath('.//td[@class="status"]/text()')[0].extract()
         
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
        if(len(main_stats) > 0):
            
            item['homePossession'] = main_stats.xpath('//div[@class="home"]/span/text()')[0].extract()
            self.logger.info('Home possession: %s ', item['homePossession'])
            stats.append(item['homePossession'])
            
            item['awayPossession'] = main_stats.xpath('//div[@class="away"]/span/text()')[0].extract()
            self.logger.info('Away possession: %s ', item['awayPossession'])
            stats.append(item['awayPossession'])
            
            stats_table = response.xpath('//div[@class="box-content ab-content"]/table')  
            
            stats = stats_table.xpath('.//td[@class="stat-value"]/text()').extract()
            siteLabels = stats_table.xpath('.//td[@class="stat-name"]/text()').extract()

            outputTable.append(item['homeTeam']  + ' | ' +  item['scoreboard'] + ' | ' + item['awayTeam'])
            outputTable.append(':-:|:-:|:-:')
            outputTable.append(item['homePossession'] + ' | Possesion | ' + item['awayPossession'])
            
            for s in range(len(stats)):
                
                if(s%2 != 0 and (s<len(stats))):
                    labelToTranslate = siteLabels[int((s-1)/2)]
                    printLabel = ''
                   
                    if(labelToTranslate not in translations):
                        printLabel = labelToTranslate
                    else:
                        printLabel = translations[labelToTranslate]

                    outputTable.append(stats[s-1] + ' | ' + printLabel  + ' | ' + stats[s])
                              
            item['statTable'] = ' \n'.join(outputTable)
        
            yield item
            yield scrapy.Request(url=response.url, callback=self.parseLiveMatch, dont_filter=True)
        else:
            item['errors'] = 'No stats available for this game.'
            yield item
            #yield scrapy.Request(url=response.url, callback=self.parseLiveMatch, dont_filter=True)
        
