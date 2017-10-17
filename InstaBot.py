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
            print 'Username= %s ' %(user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'


#self_info()
#get_user_id('rajat8310')
get_user_info('rajat8310')