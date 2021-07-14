# Reddit-To-Insta
make a self building insta page

The programme runs fine in python 3.9.6

Developer: https://twitter.com/GamesJackhammer or https://www.instagram.com/jackhammer_games/

Known Issues:
Video not uploading even when status returns ok

REQUIREMENTS:

An instagram account
A Reddit Application set up look at: https://www.reddit.com/prefs/apps

Libraries:
Praw 
Instabot
Pillow
(rest are in built)

What You Need To Know:
Your reddit application's Client ID and Client_Secret 

How Do I Start Using It?
=> you need to do couple a things before you can start your own self-building insta page
=> make sure your reddit application is set up proplerly and place your client id , client secret , bot name , reddit account username and reddit account password in the praw initialize method
=> Enter your instagram user id and password in Bot() method as well
=> look for captionsPost list and add your instagram captions, tailor them according to your needs
=> the programme which choose a random caption for each post 
=> make sure you have a data.txt file in your script location
=> run the bot and see it do it's magic!
=> Bot should upload evrey 15 minutes OR more

Will my account get blocked?
=> unless you have a decent time between uploading posts you are good to go!
=> Instagram actually allows unlimited post uploads unlike other restricted things like liking , commenting / hourly basis after which you get rated limited!
=> in theory you could upload infinitley but that'd make lots of requests and get your insta blocked for few hours
=> Hence it's neccessary to have delay between posts.

ADDITIONAL:
=> you can upload your project to heroku or other cloud computing service to run it 24/7 :)
