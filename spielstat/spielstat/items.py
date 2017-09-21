# -*- coding: utf-8 -*-
# spielstat items
#
# @author: nachos
# github.com/imnachos/spielstat


import scrapy


class SpielstatItem(scrapy.Item):
    
    """
        Item for storing match stats
    """ 
    errors = scrapy.Field()
    
    statTable = scrapy.Field()
    scoreboard = scrapy.Field()
    updateTime = scrapy.Field()
    
    homeTeam = scrapy.Field()
    awayTeam = scrapy.Field()
   
    homeGoals = scrapy.Field()
    awayGoals = scrapy.Field()

    homePossession = scrapy.Field()
    awayPossession = scrapy.Field()
