'''This module is used to fetch date and time'''
#Function to get date
import datetime
def getDate():

    now = datetime.datetime.now
    return str(now().date())

#Function to get time
def getTime():
    
    now = datetime.datetime.now
    return(str(now().time()))
