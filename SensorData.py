import pandas as pd
import numpy as np

class SensorData:
    
    def __init__(self,directory):
        
        self.users = pd.read_csv('data/USERS.csv')
        self.questionnaire = pd.read_csv('data/QUESTIONNAIRE.csv')
        self.motion = pd.read_csv('data/MOTION.csv')
        self.sound = pd.read_csv('data/SOUND.csv')
        self.location = pd.read_csv('data/LOCATION.csv')
        
        #Data Collection App had 30 test users...we will exclude them from the analysis
        self.users = self.users[self.users['userID'] >= 30]
        self.questionnaire = self.questionnaire[self.questionnaire['user'] >= 30]
        self.motion = self.motion[self.motion['user'] >= 30]
        self.sound = self.sound[self.sound['user']>= 30]
        self.location = self.location[self.location['user'] >= 30]
        
        #Remove Questionnaire entries that do not have a valid Result1 and Result2 (Result1 and Result2 are the SF36 questionnaire summary values for 
        #Physical Component Score and Mental component scores. 
        #These are summary meeasure computed from the other 36 items. Result1 and Result2 are computed at the time of completing the questionnaire on the App)
        self.questionnaire = self.questionnaire[(self.questionnaire['Result1'] > 0) & (self.questionnaire['Result2'] > 0)]
        
        #Join Questionnaire with User (do a qs left join with users so that only users with valid questionnaire data are kept in the resulting join)
        users = users.rename(columns={'userID':'user'})
        joined = pd.merge(qs,users,on='user',how='left')
        
        