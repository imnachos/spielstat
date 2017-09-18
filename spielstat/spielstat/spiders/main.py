# -*- coding: utf-8 -*-

import logging
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.project import get_project_settings
import json

class SpielstatSpider(scrapy.Spider):

    name = 'spielstat'
    
    def start_requests(self):
        urls = [
            'http://www.marcadores.com/futbol/espana/liga-bbva/espanyol-celta-m10577697.html'
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
	
    def parse(self, response):
        self.logger.info('Parse called on: %s', response.url)
        self.logger.info('Response body: %s', response.body)
        container = response.xpath("/html/body[@id='page_match_live']/div[@id='wrapper']/div[@class='site-holder']/div[@class='main-area']/div[@id='main']/div[@class='page-container']/div[@id='content']/div[@class='content-frame']/div[@class='content-column']/div[@class='content-inner']/div[@id='box_4946215']/div[@class='box-content ab-content']/table/tbody/tr[1]/td[@class='stat-value'][1]")
        self.logger.info('Log: %s ', container)
	