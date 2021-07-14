from instabot import Bot
import os 
import glob
import praw
import requests
import time
import urllib.request
import random
from PIL import Image  

uploaded = []
with open ("data.txt", "r") as myfile:
    for item in myfile.readlines():
        uploaded.append(item.replace('\n', '')) #remove new lines from data returned

def Upload(link , title , author):
    Captions = [
        f'{title} \n credits: {author} on reddit \n YOUR HASHTAGS HERE' , # list of different captions for post, modify them as per your wish
        f'{title} \n credits: {author} on reddit \n YOUR HASHTAGS HERE' ,
        f'{title} \n credits: {author} on reddit \n YOUR HASHTAGS HERE'
    ]
    captionPost = Captions[random.randint(0,len(captions)-1)] #choosing random caption for post
    try:
        if postType == 'i':
            bot.upload_photo(link, caption=captionPost)
        else:
            bot.upload_video(link , caption = captionPost) #video posting might not work i am lokking into a solution
        print("sleeping for 15 minutes")
        time.sleep(15*60) #sleep after posting for 5 minutes so not to spam API
    except Exception as e:
        print(e)
        print("Something Was Wrong Not sure what")


try:
    cookie_del = glob.glob("config/*cookie.json") # deleting older cookies as instabot acts weird sometimes
    os.remove(cookie_del[0])
except:
    pass
bot = Bot()
bot.login(username="your instagram username", password="your instagram pass")

reddit = praw.Reddit(
    client_id="Praw client id here",
    client_secret="praw client secret here",
    user_agent="enter the name of bot",
    username="reddit username",
    password="reddit account password",
)

while True:
    for submission in reddit.subreddit("dankmemes").new(): #choose subreddit of choice here you can use .new() , .hot() , .top() as methods you can pass an argument limit to scrape limited posts like .new(limit=10)
        print("\n Checking Submission At: " , submission.url)
        try:
            request = requests.get(submission.url)
        except:
            pass
        url = submission.url
        postType = ''
        Eligible = True
        for x in uploaded: #checking if post has already been uploaded 
            if url in x:
                Eligible = False
                print("Post Already Posted" , submission.url)

        if submission.is_self == False and Eligible == True: #making sure that post on reddit is NOT text post and image one or video one only
            if "jpg" in url or "png" in url or "jpeg" in url:
                
                print("Type Detected: Image")
                try:
                    print("removing remove me file")
                    os.remove("PostContent.jpeg.REMOVE_ME") #attempt to remove this file as it causes errors
                except:
                    print("No remove me file found")
                try:
                    img_data = request.content #storing image data 
                    file = open('PostContent.jpeg' , 'wb') #image name
                    file.write(img_data)
                    name = file.name
                    postType = 'i'
                    file.close()
                except:
                    pass
                try:
                    print("Reszing the image....") #resizing image size to fit aspect ratio
                    im = Image.open("PostContent.jpeg")  
                    newsize = (1080, 1080) 
                    im1 = im.resize(newsize) 
                    im.save('PostContent.jpeg')
                except Exception as e:
                    print(e)
                    print("Error While Resizing")
            else:
                try:
                    if 'v.redd' in submission.url:
                        print("Type detected: Video")
                        url = submission.media["reddit_video"]["fallback_url"]  #getting the source of reddit video
                        print("retriving video")
                        urllib.request.urlretrieve(url,"VideoContent.mp4")
                        postType = 'v'
                except Exception as e:
                    print(e)
                    print("error while retriving vieo for url " , url)
                    
            try:
                if postType == 'v': #checking for video post
                    file = open('VideoContent.mp4' , 'rb')
                    name = file.name
                    file.close()
                    Upload(name , submission.title , submission.author) #uploading video file
                elif postType == 'i': #checking for image post
                    print("Uploading Image.....")
                    file = open('PostContent.jpeg' , 'rb')
                    name = file.name
                    file.close()
                    uploaded.append(submission.url) #adding url to the data file
                    with open('data.txt', 'w') as f:
                        for item in uploaded:
                            f.write(f"{item} \n")
                    Upload(name , submission.title , submission.author)
                pass
            except Exception as e:
                print(e)
                pass
        else:
            print("Ignoring Text Post At: ",submission.url)
