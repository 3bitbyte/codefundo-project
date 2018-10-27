# codefundo-project
Natural disaster alert system

What we are planning to build:
	A 'Potential alert system' using social media(Twitter) at the inception of a disaster.
	
	-By the time a natural disaster is first being reported in a official news site(relatively slow medium),
         it becomes a fast spreading news in social media like Twitter, Facebook, Reddit etc due to the immediacy 
         quality of social media.

	Some instances to prove:
		-The China Earthquake:
			In 2008, tweets from China alerted the world to the region's severe earthquake, before the United 
		States Geological Survey commented.

		-The Virigina earthquake:
			In 2011, Virigina earthquake spread on Twitter faster than many people felt the shocks in real life
		Twitter later revealed that more than 40,000 earthquake-related tweets were sent within a minute of 
		its occurrence.

	Reason for Twitter as social medium:
		-The American Press Institute, Twitter and a research company DB5, produced a study which gives
		 insight on the relationship between news use and Twitter-sphere. The study, involving 4,700 
		 social media users, found out that Twitter users are more inclined to news than other social media users.
		-Tweets are short(max 280 words), easy to analyze and extract information.
		-Twitter's API platform provides broad access to public Twitter data that users have chosen to 
		 share with the world.
		
	Reliability consciousness:
		-Tweets from twitter may be fake.
		-It can be overcome by, setting some threshold value on the number of tweets. Since, it is highly unlikely
		 that 100 regular twitter users tweet fake instances at the same time.
		-If every tweet is exactly the same, then it's more likely to be fake.
		 For example, initially a user posted a fake tweet regarding a natural disaster, seeing this many users
		 with a mindset to create awareness might re-tweet the same fake post.
		 	
	How it works:
		-Soon after the beginning of a disaster, people around and near by the site of disaster tweet about it.
		-Our python application continuously analyses the streaming tweets around the world which are
		 related to natural disasters, using Twitter API and tweepy.
		-Tweets containing keywords like "floods","earthquake","hurricane","tornadoes" etc... are our interests.
		-The 'type of disaster' with its location can be easily obtained using 'geo-tag' of the tweets,
		 or the location of the user.
		-Casualty count and death toll can be extracted from the tweets using natural language processing to
		 some level of reliability.
		-This information helps in taking further recovery measures necessary.

	Getting started with the project:
		-The main application running on the server tracks frequency of tweets from a location about disasters.
		 Once the threshold is reached, it passes the message to the human moderator who resolves the credibility issues.

	Datasets used:
		-Stream of real-time tweets related to disasters.

	Technologies used:
		-Python
		-Twitter API
		-Natural Language Processing

	Feasibility:
		-We believe our project is much feasible since there is no need of any NEW electronic device or tech.
		-The application will simply work on devices across platforms, notify the user about any disaster happening around
		 them in seconds.
