# -*- coding: utf-8 -*-
# spielstat items
#
# @author: nachos
# github.com/imnachos/spielstat

import logging
import praw
import time

from scrapy.utils.project import get_project_settings

class SpielstatPipeline(object):
    
    print('Start pipeline.')

    def __init__(self):
        print('Initialize pipeline.')

    def open_spider(self, spider):
        print('Open spider.')

    def close_spider(self, spider):
        print('Close spider.')

        
    def checkBotSubredditForMatch(self, home, away, reddit, spider):
        reddit = praw.Reddit('spielstat')   
        subreddit = reddit.subreddit(spider.settings['BOT_SUBREDDIT'])
        
        for submission in subreddit.hot(limit=spider.settings['HOT_LIMIT']):
            if(home in (submission.title) and away in (submission.title)):
                return submission
    
        
        postTitle = home + ' - ' + away +  ' | ' + time.strftime("%d/%m/%Y")
        returnPost = subreddit.submit(title=postTitle , selftext='Updating...')
        return returnPost
        
    def getCommentBody(self, isPM, item):
        baseBody = '**Spielbot stats:** \n\n *Last update:* ' + item['updateTime'] + ' \n\n '
        if('errors' not in item):
            if(isPM):
                commentedTable = '#' + item['statTable']
                commentBody =  baseBody +  commentedTable
            else:
                commentBody = baseBody +  item['statTable']
        else:
            miniTable = item['homeTeam']  + ' | ' +  item['scoreboard'] + ' | ' + item['awayTeam'] + ' \n\n ' + ':-:|:-:|:-:'
            commentBody = baseBody +  miniTable
            
        return commentBody
    
    def process_item(self, item, spider):
        print('Post item:', item['scoreboard'])
        
        reddit = praw.Reddit('spielstat')  
            
        doesCommentExist = False
        commentFooter = '\n\n *I am a bot! Please [PM me](https://www.reddit.com/message/compose/?to=Spielstat_bot) if I\'ve been naughty :)*'

        
        if(spider.settings['SCRAPE_LEAGUES'] == False):
        
            subreddit = reddit.subreddit(spider.settings['TEAM_SUBREDDIT']) 
            if('Fin' in item['updateTime']):
                commentBody = self.getCommentBody(True, item)
                completeComment = commentBody + commentFooter
            
                for submission in subreddit.hot(limit=3):
                
                    if('Post ' in (submission.title)):
                        postAuthor = submission.author
                        postAuthor.message('Spielstat match stats.', completeComment, from_subreddit=None)
                        self.logger.info('Match finished. Sent PM to Post Game Thread author.')
                        spider.close()
            else:
                liveThread = ''
                commentBody = self.getCommentBody(False, item)
                completeComment = commentBody + commentFooter
                
                for submission in subreddit.hot(limit=3):
                    if('Game Thread' in (submission.title) and 'Post' not in submission.title):
                        comments = submission.comments.list()
                        liveThread = submission.url
                        
                        for comment in comments:
                            if(comment.author == 'Spielstat_bot'):
                                doesCommentExist = True
                                
                        if(doesCommentExist == False):
                            submission.reply(completeComment)
                        else:
                            comment.edit(completeComment)
                
                #Post to live thread
                if(spider.settings['TEAM_LIVE_THREAD']):
                    liveID = liveThread[28:]
                    liveThread = reddit.live(liveID)
                    #liveThread.contrib.add(completeComment)
                           
        else:
            subreddit = reddit.subreddit(spider.settings['BOT_SUBREDDIT'])
            commentBody = self.getCommentBody(False, item)
            completeComment = commentBody + commentFooter
            
            submission = self.checkBotSubredditForMatch(item['homeTeam'], item['awayTeam'], reddit, spider)
            
            if('Fin' not in submission.selftext):
                submission.edit(completeComment)
                      
        return item