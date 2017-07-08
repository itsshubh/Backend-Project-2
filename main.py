import requests, urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

access_token = '1429837265.d9f119e.9245cb90633d4a60abf732429c216e95'
base_url = 'https://api.instagram.com/v1/'

# Function(a) declaration to get your own info
def self_info():

    request_url = (base_url + 'users/self/?access_token=%s')%(access_token)
    print 'GET request url: %s'%(request_url)
    user_info = requests.get(request_url).json()

    try:

        if user_info['meta']['code'] == 200:
            if len(user_info['data']):
                print 'Username:-%s' % (user_info['data']['username'])
                print 'Your total number of followers are:%s.' %(user_info['data']['counts']['followed_by'])
                print 'You follows %s people.' %(user_info['data']['counts']['follows'])
                print 'You have total %s posts.' %(user_info['data']['counts']['media'])
            else:
                print 'User does not exist'
        else:
            print 'Status Code = %s, which is not 200.' %(user_info['meta']['code'])
            exit()
    except:
        print 'JSON object could not be decoded.'



# Function declaraiton to get the ID of a user by Username
def get_user_id(insta_username):

    request_url = (base_url + 'users/search?q=%s&access_token=%s')%(insta_username, access_token)
    print 'GET request url(with username) : %s' %(request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status Code = %s, which is not 200.' % (user_info['meta']['code'])
        exit()



# Function(b) declaration to get the info of a user by username
def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'


    request_url = (base_url + 'users/%s?access_token=%s') % (user_id, access_token)
    print 'GET request url(with user id) : %s' % (request_url)

    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username:-%s' % (user_info['data']['username'])
            print 'Your total number of followers are:%s.' %(user_info['data']['counts']['followed_by'])
            print 'You follows %s people.' %(user_info['data']['counts']['follows'])
            print 'You have total %s posts.' %(user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user.'
    else:
        print 'Status Code = %s, which is not 200.' %(user_info['meta']['code'])



# Function(c) declaration to get your recent post.
def get_own_post():
    request_url = (base_url +'users/self/media/recent/?access_token=%s')%(access_token)
    print"GET request url : %s" %(request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print "Your image has been downloaded."
            print "and the post id is:-%s" %(own_media['data'][0]['id'])

            # finding the post with minimum number of likes.
            likes_count = []
            for a in range(0, len(own_media['data'])):
                likes_count.append(own_media['data'][a]['likes']['count'])
            # list.index(max(list))   --- to find the index
            print 'the url of post with minnimum number of likes are:', \
            own_media['data'][likes_count.index(min(likes_count))]['images']['standard_resolution']['url']

        else:
            print "Post does not Exist."
    else:
        print 'Status Code = %s, which is not 200.' % (own_media['meta']['code'])



# Function(d) declaration to get the user's post using insta username.
def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print "User does not exist!"
        exit()
    request_url = (base_url + 'users/%s/media/recent/?access_token=%s') %(user_id,access_token)
    print "GET request url: %s" %(request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print "Your image has been downloaded."
            print "and the post id is:-%s" %(user_media['data'][0]['id'])

            # finding the post with minimum number of likes.
            likes_count = []
            for a in range(0, len(user_media['data'])):
                likes_count.append(user_media['data'][a]['likes']['count'])
            # list.index(max(list))   --- to find the index
            print 'the url of post with minnimum number of likes are:', \
                user_media['data'][likes_count.index(min(likes_count))]['images']['standard_resolution']['url']

        else:
            print "Post does not Exist."
    else:
        print 'Status Code = %s, which is not 200.' % (user_media['meta']['code'])



# Function declaration to get the recent post liked by self.
def recent_media_liked():
    request_url = (base_url + 'users/self/media/liked?access_token=%s')%(access_token)
    print "GET request URL:%s" %(request_url)
    recent_media = requests.get(request_url).json()

    if recent_media['meta']['code'] == 200:
        if len(recent_media['data']):
            image_name = recent_media['data'][0]['id']
            image_url = recent_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print "The recent media liked by the user is downloaded."



# Function declaration to get the ID of the recent post of a user by username
def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print "User does not exist!"
        exit()

    request_url = (base_url + 'users/%s/media/recent?access_token=%s')%(user_id,access_token)
    print "Get request URL:%s "%(request_url)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status Code = %s, which is not 200.' % (user_media['meta']['code'])
        exit()



# Funstion(f) declaration to like the recent post of a user
def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (base_url + 'media/%s/likes')%(media_id)
    payload = {"access_token":access_token}
    print "POST request URL: %s" %(request_url)
    post_a_like = requests.post(request_url,payload).json()
    if post_a_like['meta']['code'] == 200:
        print "LIKE was Successful"
    else:
        print "Your LIKE was Unsuccessful.Sorry"



# Function(g) declaration to get the list of comments on the post.
def list_of_comments(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (base_url + 'media/%s/comments?access_token=%s')%(media_id, access_token)
    print "Get request URL:%s"%(request_url)
    listing_comments = requests.get(request_url).json()
    if listing_comments['meta']['code'] == 200:
        if listing_comments['data']:
            comments = []
            for c in range(0,len(listing_comments['data'])):
                comments.append(listing_comments['data'][c]['text'])
            print "The comments are:\n"
            for b in comments:
                print b
        else:
            print 'No data found'
    else:
        print 'Status Code = %s, which is not 200.' % (listing_comments['meta']['code'])
        exit()



# Function(h) declaration to make a comment on the recent post of the user
def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("What do you want to comment:- ")
    payload = {"access_token": access_token, "text": comment_text}
    request_url = (base_url + 'media/%s/comments')%(media_id)
    print "POST request url: %s" %(request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "The comment has been added!!"
    else:
        print "Unable to add the comment. Sorry!"




# Now starting the itsinstabot
def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to itsinstabot'
        print 'Here are your menu options:-'
        print 'a. Get your own details.\n' \
              'b. Get details of a user by username\n' \
              'c. Get your own recent post\n' \
              'd. Get the recent post of a user by username\n' \
              'e. Get a list of people who have liked the recent post of a user\n' \
              'f. Like the recent post of a user\n' \
              'g. Get a list of comments on the recent post of a user\n' \
              'h. Make a comment on the recent post of a user\n' \
              'i. Delete negative comments from the recent post of a user\n' \
              'j. Exit'
        choice = raw_input("Enter your choice:")
        if choice == "a":
            self_info()
        elif choice == 'b':
            insta_username = raw_input("Enter the username of the user:")
            get_user_info(insta_username)
            print 'JSON object could not be decoded.'
        elif choice == 'c':
            get_own_post()
        elif choice == 'd':
            insta_username = raw_input("Enter the username of the user:")
            get_user_post(insta_username)

        elif choice == "f":
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
        elif choice == 'g':
            insta_username = raw_input("Enter the username of the user: ")
            list_of_comments(insta_username)

        elif choice == "h":
            insta_username = raw_input("Enter the username of the user: ")
            post_a_comment(insta_username)

        elif choice == "j":
            exit()
        else:
            print "WRONG CHOICE"
            print "Enter your choice again"
            start_bot()

start_bot()