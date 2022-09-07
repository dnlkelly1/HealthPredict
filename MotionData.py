import pandas as pd
import numpy as np

class MotionData:
    
    def __init__(self,directory):
           
        self.motion = self.loadMotion(directory)
        self.qs = self.loadQuestionnaire(directory)
        
        
        
        
    def loadMotion(self,directory):
        
        motion = pd.read_csv(directory + '/MOTION.csv')
        motion = motion[motion['user'] >= 30]
        
        #convert datetime to pandas datetime format and remove any rows that could not be converted (dropping NAN times is extremely rare)
        motion['datetime'] = pd.to_datetime(motion['datetime'],infer_datetime_format=True,errors='coerce')
        motion = motion.dropna(subset=['datetime'])
        #remove columns that are not useful
        motion = motion.drop(['motionEntryID','f1','f34','f35'],axis=1)
        
        return motion
        
    def loadQuestionnaire(self,directory):
        
        users = pd.read_csv(directory + '/USERS.csv')
        qs = pd.read_csv(directory + '/QUESTIONNAIRE.csv')
        
        users = users[users['userID'] >= 30]
        qs = qs[qs['user'] >= 30]
        
        #Remove Questionnaire entries that do not have a enough valid answers
        #(Result1 and Result2 are the SF36 questionnaire summary values for Physical Component Score and Mental component scores.
        #They are computed using individual questions Q1-Q37
        #To ensure that Result1 and Result2 are valid, we first check that enough of the individual questions have been answered
        #This is done by selecting just the individual questions (qs.iloc[:,3:39]) and count how many are not -1
        #If enought are valid (we set 18 as an arbitrary threshold), then we keep that record
        qs = qs[(qs.iloc[:,3:39] > 0).sum(axis=1) > 18]
        
        #If a user has multiple questionnaire entries...keep only the most recent (tail) one
        qs = qs.groupby(by='user').tail(1)
        
        #Join Questionnaire with User (do a qs left join with users so that only users with valid questionnaire data are kept in the resulting join)
        users = users.rename(columns={'userID':'user'})
        valid_questionnaire = pd.merge(qs,users,on='user',how='left')
        
        return valid_questionnaire