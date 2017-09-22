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


## Subreddit


BOT_SUBREDDIT = 'spielstat_bot'
HOT_LIMIT = 30

## Team

TEAM_TO_SCRAPE = 'http://www.marcadores.com/futbol/espana/equipo-sevilla-atletico-8088554.html'
TEAM_SUBREDDIT = 'spielstat_bot'
TEAM_LIVE_THREAD = True

## Leagues

SCRAPE_LEAGUES = False

LEAGUES_TO_SCRAPE = ['http://www.marcadores.com/futbol/francia/liga-francesa/',
            'http://www.marcadores.com/futbol/espana/liga-bbva/',
            'http://www.marcadores.com/futbol/alemania/bundesliga/',
            'http://www.marcadores.com/futbol/inglaterra/premier-league/',
            'http://www.marcadores.com/futbol/internacional/champions-league/',
            'http://www.marcadores.com/futbol/internacional/europa-league/',
            'http://www.marcadores.com/futbol/alemania/2-bundesliga/']

ROBOTSTXT_OBEY = True
COOKIES_ENABLED = False
DOWNLOAD_DELAY = 1

FEED_EXPORT_ENCODING = 'utf-8'

ALLOWED_DOMAINS = ['http://www.marcadores.com']

LOG_ENABLED = False
LOG_FILE = 'log.log'

