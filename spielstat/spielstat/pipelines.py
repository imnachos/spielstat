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
        print('Open spider.')

    def close_spider(self, spider):
        print('Close spider.')

    def process_item(self, item, spider):
        print('Post item:', item)
        reddit = praw.Reddit('spielstat') 
                     
        print(reddit.user.me())
        subreddit = reddit.subreddit(spider.settings['SUBREDDIT'])
        edited = False
        
        for submission in subreddit.hot(limit=3):
            if('Game Thread' in (submission.title)):
                comments = submission.comments.list()
                for comment in comments:
                    if(comment.author == 'Spielstat_bot'):
                        comment.edit('**Stats** \n' + item['statTable'])
                        edited = True
        
                if(edited == False):
                    submission.reply('**Stats** \n' + item['statTable'])
        return item