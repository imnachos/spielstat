# -*- coding: utf-8 -*-
# spielstat items
#
# @author: nachos
# github.com/imnachos/spielstat

import logging
import praw
from scrapy.utils.project import get_project_settings

class SpielstatPipeline(object):
    
    print('Start pipeline.')

    def __init__(self):
        print('Initialize pipeline.')

    def open_spider(self, spider):
        teamURL = spider.settings['TEAM_TO_SCRAPE']
        print('Open spider.')

    def close_spider(self, spider):
        print('Close spider.')

    def process_item(self, item, spider):
        print('Post item:', item)
        reddit = praw.Reddit('spielstat')
        subreddit = reddit.subreddit(spider.settings['SUBREDDIT'])

        
        return item