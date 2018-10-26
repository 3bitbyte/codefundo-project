import tweepy
import pandas
import numpy
import json
import vincent
import plotly.plotly as py
from plotly.offline import plot
import plotly.graph_objs as go
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
from dateutil import tz

dates=[]
text=[]

def create_api():

#Variables that contains the user credentials to access Twitter API 
    access_token = "996261467308486656-lLk59c6R3IHaBNGEGPEiIHV1yFq262b"
    access_token_secret = "mkWqxIlRDuFd6KfCgiEbGglUpt5xbrU9VReiBe4yvmd3m"
    consumer_key = "ZwrEIhjsqVNoFnwpFhakCFhLL"
    consumer_secret = "OBmxZvxSRKx5ABcAERAeRQKERzCTuPq3rz9k2UTANtsMO00CvQ"
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    return api

def get_tweets(start,end,keyword,api):
    
    global dates
    global text
    startSince = start
    endUntil = end
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    count=0
    #q='*'-----------get all tweets-----works only when geocode is given
    #geocode="20.5937,78.9629,150km"-----geocode for india
    #geocode="-0.7893, 113.9213,100km"
    for x in tweepy.Cursor(api.search,q='*',geocode="20.5937,78.9629,150km",
              since=startSince, until=endUntil,count=100).items(100):
#    decoded = json.loads(x)
#    if 'a' in decoded['text'].lower() and decoded['place']['name'].lower() is 'manhattan':
#            print('@%s : %s' % (decoded['user']['screen_name'],decoded['text']))
    
        count+=1
        #print(x)
        #print(x.created_at,count,x.user.location)
        utc = datetime.strptime(str(x.created_at), '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=from_zone)
        ist = utc.astimezone(to_zone)
        #print(x.text)
        dates.append(ist)
        text.append(x.text)
        #print(count)
    return text


def get_plot():
##    
##    ones = [1]*len(dates)
##    idx = pandas.DatetimeIndex(dates)
##    time_series_data = pandas.Series(ones, index=idx)
##    per_minute = time_series_data.resample('5Min').sum().fillna(0)
##    #print(per_minute)
##    #print(type(per_minute))
##    req1=pandas.to_datetime(per_minute)  #extract date from per_minute
##    #print(req1)
##    req2=per_minute.values #extract values(count of tweets in each window) from per_minute
##    #print(req2)
    df = pandas.DataFrame(index = dates)
    df['freq'] = numpy.repeat(1,len(dates))
    df  = df.freq.resample('5T').sum()
    data = [go.Scatter( x=df.index, y=df )]
    pl=plot(data,output_type='div')  #--------------->poomani's str object for plot
    return pl


today = datetime.now()
start = datetime.strftime(today-timedelta(1),"%Y-%m-%d")
end = datetime.strftime(today+timedelta(1),"%Y-%m-%d")
keyword='india'
api=create_api()
text=get_tweets(start,end,keyword,api)
f = open('D:\codefundo\plot.txt','w')
f.write(get_plot())
f.close()
#get_plot()
#print(text)



