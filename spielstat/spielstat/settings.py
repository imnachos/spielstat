# -*- coding: utf-8 -*-
# spielstat items
#
# @author: nachos
# github.com/imnachos/spielstat

BOT_NAME = 'spielstat'

SPIDER_MODULES = ['spielstat.spiders']
NEWSPIDER_MODULE = 'spielstat.spiders'

USER_AGENT = 'spielstat (+https://github.com/imnachos/spielstat)'

ITEM_PIPELINES = {
    'spielstat.pipelines.SpielstatPipeline': 100
}

TEAM_TO_SCRAPE = 'http://www.marcadores.com/futbol/alemania/equipo-borussia-dortmund-8006912.html'

ROBOTSTXT_OBEY = True
COOKIES_ENABLED = False

LOG_ENABLED = False
LOG_FILE = 'log.log'

SUBREDDIT = 'borussiadortmund'