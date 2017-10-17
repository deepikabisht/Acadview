import requests
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

#Function to get our own recent post

def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
    if(own_media['meta']['code']==200):
        if len(own_media['data']):
            print own_media['data'][0]['id']
        else:
            print  'Post does not exists'
    else:
        print 'Status code other than 200 received!'

# Function to fetch recent post of user by username

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
            print user_media['data'][0]['id']
        else:
            print  'Post does not exists'
    else:
        print 'Status code other than 200 received!'


# InstaBot menu

def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get recent post of a user by username\n"
        print "j.Exit"

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
        elif choice=="j":
            exit()
        else:
            print "wrong choice"

start_bot()