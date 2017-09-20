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
    
    statTable = scrapy.Field()
    
    homeTeam = scrapy.Field()
    awayTeam = scrapy.Field()
    homeGoals = scrapy.Field()
    awayGoals = scrapy.Field()
    
    scoreboard = scrapy.Field()
    
    homePossession = scrapy.Field()
    homeShotsOnGoal = scrapy.Field()
    homeMissedShots = scrapy.Field()
    homeFreekicks = scrapy.Field()
    homeCorners = scrapy.Field()
    homeOffsides = scrapy.Field()
    homeThrowIn = scrapy.Field()
    homeSaves = scrapy.Field()
    homeInfractions = scrapy.Field()
    
    awayPossession = scrapy.Field()
    awayShotsOnGoal = scrapy.Field()
    awayMissedShots = scrapy.Field()
    awayFreekicks = scrapy.Field()
    awayCorners = scrapy.Field()
    awayOffsides = scrapy.Field()
    awayThrowIn = scrapy.Field()
    awaySaves = scrapy.Field()
    awayInfractions = scrapy.Field()