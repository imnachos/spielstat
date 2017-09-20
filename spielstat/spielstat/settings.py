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

#TEAM_TO_SCRAPE = 'http://www.marcadores.com/futbol/alemania/equipo-borussia-dortmund-8006912.html'
TEAM_TO_SCRAPE = 'http://www.marcadores.com/futbol/espana/equipo-real-madrid-8005756.html'

FEED_EXPORT_ENCODING = 'utf-8'

ALLOWED_DOMAINS = ['www.marcadores.com']

ROBOTSTXT_OBEY = True
COOKIES_ENABLED = False
DOWNLOAD_DELAY = 10

LOG_ENABLED = False
LOG_FILE = 'log.log'
LOG_STDOUT = True

SUBREDDIT = 'spielstat_bot'