import requests
BASE_URL= 'https://api.instagram.com/v1/'
APP_ACCESS_TOKEN= '4870715640.a48e759.874aba351e5147eca8a9d36b9688f494'
def self_info():
    request_url= (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()


self_info()