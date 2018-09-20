# spielstat
A sample project on how to use scrapy and integrate it with reddit.

# Installation

Make sure you have praw and scrapy installed.

```
pip install praw

pip install scrapy
```

Clone the repository.

# Bot behaviour

There are a couple of main variables defined in the configuration file, but the most importante one is:

```
SCRAPE_LEAGUES 
```
This determines if the bot uses LEAGUES_TO_SCRAPE or TEAM_TO_SCRAPE. 

If **FALSE**, you **need** to set TEAM_SUBREDDIT, otherwise the bot won't work.

If **TRUE**, you **need** to set BOT_SUBREDDIT, otherwise the bot won't work.


# Configuration (settings.py)

BOT_SUBREDDIT = Subreddit to post the updates to if SCRAPE_LEAGUES is FALSE.

HOT_LIMIT = How far should the bot go the find if a math thread already exists. (Typically, 30 is enough)

TEAM_TO_SCRAPE = A string of the team's page. If SCRAPE_LEAGUES is FALSE, this URL will be used.

TEAM_SUBREDDIT = The team's subreddit to post the updates to.

SCRAPE_LEAGUES = If this is TRUE, the bot will use the urls in LEAGUES_TO_SCRAPE.

LEAGUES_TO_SCRAPE = Direct URL to the leagues.

DOWNLOAD_DELAY = How often should the bot update. Please don't use a low value. (seconds)

# Running the bot
Go to the spider's directory.

```
cd "...\spielstat\spielstat\spielstat\spiders"
```
Run the spider.

```
scrapy crawl spielstat
```
