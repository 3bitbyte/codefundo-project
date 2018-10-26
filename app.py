from datetime import datetime,timedelta
import tweepy
import pandas
import numpy
import json
import vincent
from datetime import datetime
#import matplotlib.pyplot as plt
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
    
    global dates,text
    text=[]
    dates=[]
    startSince = start
    endUntil = end
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    count=0
    
    for x in tweepy.Cursor(api.search,  
              q=keyword,geocode=locat,
              since=startSince, until=endUntil,count=100).items(100):
#    decoded = json.loads(x)
#    if 'a' in decoded['text'].lower() and decoded['place']['name'].lower() is 'manhattan':
#            print('@%s : %s' % (decoded['user']['screen_name'],decoded['text']))
    
        count+=1
        utc = datetime.strptime(str(x.created_at), '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=from_zone)
        ist = utc.astimezone(to_zone)
        dates.append(ist)
        text.append(x.text)

    
import webbrowser
from flask import Flask,request
from flask import render_template as rn
from random import sample
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objs as go
from flask import Markup

def get_plot():
    df = pandas.DataFrame(index = dates)
    df['freq'] = numpy.repeat(1,len(dates))
    df  = df.freq.resample('5T').sum()
    data = [go.Scatter( x=df.index, y=df )]
    pl=plot(data,output_type='div')  #--------------->poomani's str object for plot
    return pl

app = Flask(__name__)

locat = "20.5937,78.9629,6000km"
start = ""
end = ""
keyword = ""
api = ""

@app.route('/')
def hello():
    return rn('forms.html')

@app.route('/process',methods=['POST','GET'])
def hello2():
    calamity = request.form['calamity']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    tradius = request.form['radius']
    global locat,start,end,keyword,api
    if latitude != "" and longitude!= "" and tradius != "":
        locat = latitude+","+longitude+","+tradius+"km"

    today = datetime.now()
    start = datetime.strftime(today-timedelta(1),"%Y-%m-%d")
    end = datetime.strftime(today+timedelta(1),"%Y-%m-%d")
    keyword=calamity
    api=create_api()
    
    #get_tweets(start,end,keyword,api)
    return rn('temp.html')

@app.route('/results')
def results():
    
    global locat,start,end,keyword,api
    get_tweets(start,end,keyword,api)
    
    my_plot_div = get_plot()
    #my_plot_div = plot([Scatter(x=x,y=y)], output_type='div')
    return rn('results.html',div_placeholder=Markup(my_plot_div),users=text)


if __name__ == '__main__':
    app.run(debug=True)
