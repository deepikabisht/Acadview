import requests
import urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

BASE_URL= 'https://api.instagram.com/v1/'
APP_ACCESS_TOKEN= '4870715640.a48e759.874aba351e5147eca8a9d36b9688f494'
#APP_ACCESS_TOKEN = '5629236876.1cc9688.86db895c038043b5960dc2949785299a'

#Function to get own info

def self_info():
    request_url= (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'

#Function to get user_id

def get_user_id(insta_username):
    request_url= (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info= requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()

# Function to get user information

def get_user_info(insta_username):
    user_id=get_user_id(insta_username)
    if(user_id==None):
        print 'User does not exists'
        exit()
    request_url=(BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url = %s '% (request_url)
    user_info= requests.get(request_url).json()
    if(user_info['meta']['code']==200):
        if len(user_info['data']):
            print 'User id: %s '% (user_id)
            print 'Username: %s ' %(user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'

#Function to download our  own posted image

def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
    if(own_media['meta']['code']==200):
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'

        else:
            print  'Post does not exists'
    else:
        print 'Status code other than 200 received!'

# Function to fetch recent image  posted by user with minimum no of likes

def get_user_post(insta_username):
    user_id=get_user_id(insta_username)
    if(user_id==None):
        print 'User does not exists'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id,APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
    if(user_media['meta']['code']==200):
        if len(user_media['data']):
            c=len(user_media['data'])
            i=1
            m=(user_media['data'][0]['likes']['count'])
            c=c-1
            while(c!=0):
                 if(m>=(user_media['data'][i]['likes']['count'])):
                     m=(user_media['data'][i]['likes']['count'])
                     j=i
                 i=i+1
                 c=c-1

            print j
            image_name = user_media['data'][j]['id'] + '.jpeg'
            image_url = user_media['data'][j]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'


        else:
            print  'Post does not exists'
    else:
        print 'Status code other than 200 received!'


# Function to get the list of people who have liked user post by username
def get_like_list(insta_username):
    media_id=get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (media_id,APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_like = requests.get(request_url).json()
    if (user_like['meta']['code'] == 200):
        if len(user_like['data']):
            c=len(user_like['data'])
            while(c!=0):
                print 'Username: %s' % (user_like['data'][0]['username'])
                print 'Full name: %s' % (user_like['data'][0]['full_name'])
                print 'Id: %s' % (user_like['data'][0]['id'])
                c=c-1

        else:
            print  'Post does not exists'
    else:
        print 'Status code other than 200 received!'


#Function to fetch user post id by username
def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if (user_id == None):
        print 'User does not exists'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    user_media = requests.get(request_url).json()
    if (user_media['meta']['code'] == 200):
        if len(user_media['data']):
            return user_media['data'][0]['id']

        else:
            print  'Post does not exists'
    else:
        print 'Status code other than 200 received!'


#Function to like a post of a user by username

def like_a_post(insta_username):
    media_id= get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if (post_a_like['meta']['code']==200):
        print 'Like was successful'
    else:
        print 'Your like was unsuccessful. Try again!'

# Function to get the list of comments on user post by username

def get_comment_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_comment = requests.get(request_url).json()
    if (user_comment['meta']['code'] == 200):
        if len(user_comment['data']):
            c = len(user_comment['data'])
            print c
            i=0
            while (c != 0):
                print i+1
                print 'Comment from: %s' % (user_comment['data'][i]['from']['username'])
                print 'Comment text : %s' % (user_comment['data'][i]['text'])
                print 'Comment Id: %s' % (user_comment['data'][i]['id'])
                i=i+1
                c = c - 1


        else:
            print  'Post does not exists'
    else:
        print 'Status code other than 200 received!'


#Function to make a comment on user post by username
def post_a_comment(insta_username):
    media_id=get_post_id(insta_username)
    comment_text= raw_input("Enter a comment")
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)
    make_comment = requests.post(request_url, payload).json()
    if (make_comment['meta']['code'] == 200):
        print 'Successfully added a new comment'
    else:
        print 'Your comment was unsuccessful. Try again!'

#Function to delete negative comments

def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    comment_info = requests.get(request_url).json()
    if (comment_info['meta']['code'] == 200):
        if len(comment_info['data']):
            c=len(comment_info['data'])
            i=0
            j=0
            while(c!=0):
                blob = TextBlob(comment_info['data'][i]['text'], analyzer=NaiveBayesAnalyzer())
                if(blob.sentiment[0]=='neg'):
                    j=j+1
                    comment_id=comment_info['data'][i]['id']
                    del_url= (BASE_URL + 'media/%s/comments/%s?access_token=%s') %(media_id,comment_id,APP_ACCESS_TOKEN)
                    del_info= requests.delete(del_url).json()
                    if(del_info['meta']['code']==200):
                        print 'Comment deleted successfully'
                    else:
                        print 'Comment not deleted '

                i=i+1
                c=c-1
            if(j==0):
                print 'No negative comments'

        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'
    print ' GET request url : %s' % (request_url)

#Function to delete comments with particular word

def delete_using_word(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    comment_info = requests.get(request_url).json()
    if (comment_info['meta']['code'] == 200):
        if len(comment_info['data']):
            c = len(comment_info['data'])
            del_word = raw_input("enter the word : ")
            i = 0
            j = 0
            m = 0
            while (c != 0):
                s=comment_info['data'][i]['text']
                if del_word in s:
                    j=j+1
                    comment_id = comment_info['data'][i]['id']
                    del_url = (BASE_URL + 'media/%s/comments/%s?access_token=%s') % (media_id,comment_id,APP_ACCESS_TOKEN)
                    del_info = requests.delete(del_url).json()
                    if (del_info['meta']['code'] == 200):
                        m=m+1
                    else:
                        m=0

                i=i+1
                c=c-1
            if(m>0):
                print 'Comment with %s  word deleted successfully' % (del_word)
            elif(m==0):
                print  'Comment with %s word cannot be deleted' % (del_word)
            else:
                pass
            if(j==0):
                print  'No such word in the comments'
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'

    print 'GET request url : %s' % (request_url)



# InstaBot menu

def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get recent post of a user with minimum no of likes\n"
        print "e.Get the list of user who liked user post by username\n"
        print "f.Like a post of a user by username \n"
        print "g.Get the list of comment in post by username \n"
        print "h.Make a comment in user post by username \n"
        print "i.Delete negative comments \n"
        print "j.Delete comments with the particular word \n"
        print "k.Exit"

        choice=raw_input("Enter you choice: ")
        if choice=="a":
            self_info()
        elif choice=="b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice=="c":
            get_own_post()
        elif choice=="d":
            insta_username= raw_input("Enter the username of the user : ")
            get_user_post(insta_username)
        elif choice=="e":
            insta_username= raw_input("Enter the username of the user : ")
            get_like_list(insta_username)
        elif choice=="f":
            insta_username = raw_input("Enter the username of the user : ")
            like_a_post(insta_username)
        elif choice=="g":
            insta_username = raw_input("Enter the username of the user : ")
            get_comment_list(insta_username)
        elif choice=="h":
            insta_username = raw_input("Enter the username of the user : ")
            post_a_comment(insta_username)
        elif choice=="i":
            insta_username = raw_input("Enter the username of the user : ")
            delete_negative_comment(insta_username)
        elif choice == "j":
            insta_username = raw_input("Enter the username of the user : ")
            delete_using_word(insta_username)

        elif choice=="k":
            exit()
        else:
            print "wrong choice"

start_bot()