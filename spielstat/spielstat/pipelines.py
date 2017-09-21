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
                     
        subreddit = reddit.subreddit(spider.settings['SUBREDDIT'])
        
        doesCommentExist = False
          
        if('Fin' in item['updateTime']):
        
            commentedTable = '#' + item['statTable']
            commentBody = '**Spielbot stats:** \n\n *Last update:* ' + item['updateTime'] + ' \n\n ' +  commentedTable
            commentFooter = '\n\n *I am a bot! Please [PM me](https://www.reddit.com/message/compose/?to=Spielstat_bot) if I\'ve been naughty :)*'
            completeComment = commentBody + commentFooter
        
            for submission in subreddit.hot(limit=3):
            
                if('Post ' in (submission.title)):
                    postAuthor = submission.author
                    postAuthor.message('Spielstat match stats.', completeComment, from_subreddit=None)
                    self.logger.info('Match finished. Sent PM to Post Game Thread author.')
                    spider.close()
        else:         
            commentBody = '**Spielbot stats:** \n\n *Last update:* ' + item['updateTime'] + ' \n\n ' +  item['statTable']
            commentFooter = '\n\n *I am a bot! Please [PM me](https://www.reddit.com/message/compose/?to=Spielstat_bot) if I\'ve been naughty :)*'
            completeComment = commentBody + commentFooter
            
            for submission in subreddit.hot(limit=3):
                if('Game Thread' in (submission.title) and 'Post' not in submission.title):
                    comments = submission.comments.list()
                    for comment in comments:
                        if(comment.author == 'Spielstat_bot'):
                            doesCommentExist = True
                            
                    if(doesCommentExist == False):
                        self.logger.info('Comment posted.')
                        submission.reply(completeComment)
                    else:
                        self.logger.info('Comment edited.')
                        comment.edit(completeComment)
                    
        return item