# spielstat
A simple python live football feed with reddit integration.

#Installation

Make sure you have praw and scrapy installed.

```
pip install praw

pip install scrapy
```

Clone the repository.

#Configuration

DUMP_TO_BOT_SUBREDDIT = Post the matches to the Subreddit defined in BOT_SUBREDDIT
BOT_SUBREDDIT = Subreddit to post the updates to
HOT_LIMIT = How far should the bot go the find if a math thread already exists (Typically, 30 is enough)

TEAM_TO_SCRAPE = A string of the team's page. If SCRAPE_LEAGUES is FALSE, this URL will be used.
TEAM_SUBREDDIT = The team's subreddit to post the updates to.

SCRAPE_LEAGUES = If this is TRUE, the bot will use the urls in LEAGUES_TO_SCRAPE.
LEAGUES_TO_SCRAPE = ['http://www.marcadores.com/futbol/francia/liga-francesa/',
            'http://www.marcadores.com/futbol/espana/liga-bbva/',
            'http://www.marcadores.com/futbol/alemania/bundesliga/',
            'http://www.marcadores.com/futbol/inglaterra/premier-league/',
            'http://www.marcadores.com/futbol/internacional/champions-league/',
            'http://www.marcadores.com/futbol/internacional/europa-league/',
            'http://www.marcadores.com/futbol/alemania/2-bundesliga/']

DOWNLOAD_DELAY = How often should the bot update. Please don't use a low value. (seconds)

#Running the bot
Go to the spider's directory.

```
cd "...\spielstat\spielstat\spielstat\spiders"
```
Run the spider.

```
scrapy crawl spielstat
```
