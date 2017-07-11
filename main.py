#       ALL THE OBJECTIVES WILL RUN USING MY INSTAGRAM USERNAME _shubham.jain . THE USERNAME OF MY SANDBOX USERS ARE-   rishabharora47, iamhssingh..
#       FOR MY VARIANT OF TARGETED COMMENTS USE THE FOLLOWING DATA TO GET THE APPROPRIATE RESULTS..
#                                                       TAG-    udaipur


import requests, urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from termcolor import cprint

access_token = '1429837265.d9f119e.9245cb90633d4a60abf732429c216e95'
base_url = 'https://api.instagram.com/v1/'

# Function(a) declaration to get your own info
def self_info():

    request_url = (base_url + 'users/self/?access_token=%s')%(access_token)
    cprint('GET request url: %s'%(request_url),'blue')
    user_info = requests.get(request_url).json()

    try:

        if user_info['meta']['code'] == 200:
            if len(user_info['data']):
                cprint('Username:-%s' % (user_info['data']['username']),'green')
                cprint('Your total number of followers are:%s.' %(user_info['data']['counts']['followed_by']),'green')
                cprint('You follows %s people.' %(user_info['data']['counts']['follows']),'green')
                cprint('You have total %s posts.' %(user_info['data']['counts']['media']),'green')
            else:
                cprint('User does not exist','green')
        else:
            print 'Status Code = %s, which is not 200.' %(user_info['meta']['code'])
            exit()
    except:
        cprint('EXCEPTION--JSON object could not be decoded.', 'red')



# Function declaraiton to get the ID of a user by Username
def get_user_id(insta_username):
    try:
        request_url = (base_url + 'users/search?q=%s&access_token=%s')%(insta_username, access_token)
        cprint('GET request url(with username): %s'%(request_url),'blue')
        user_info = requests.get(request_url).json()

        if user_info['meta']['code'] == 200:
            if len(user_info['data']):
                return user_info['data'][0]['id']
            else:
                return None
        else:
            cprint('Status Code = %s, which is not 200.' % (user_info['meta']['code']),'green')
            exit()
    except:
        cprint('EXCEPTION--JSON object could not be decoded.', 'red')



# Function(b) declaration to get the info of a user by username
def get_user_info(insta_username):

    user_id = get_user_id(insta_username)
    if user_id == None:
        cprint('User does not exist!','green')

    try:
        request_url = (base_url + 'users/%s?access_token=%s') % (user_id, access_token)
        cprint('GET request url(with user id): %s' % (request_url), 'blue')
        user_info = requests.get(request_url).json()

        if user_info['meta']['code'] == 200:
            if len(user_info['data']):
                cprint('Username:-%s' % (user_info['data']['username']), 'green')
                cprint('Your total number of followers are:%s.' % (user_info['data']['counts']['followed_by']), 'green')
                cprint('You follows %s people.' % (user_info['data']['counts']['follows']), 'green')
                cprint('You have total %s posts.' % (user_info['data']['counts']['media']), 'green')
            else:
                cprint('There is no data for this user.','green')
        else:
            cprint('Status Code = %s, which is not 200.' % (user_info['meta']['code']), 'green')
    except:
        cprint('EXCEPTION--JSON object could not be decoded.', 'red')


# Function(c) declaration to get your recent post.
def get_own_post():
    request_url = (base_url +'users/self/media/recent/?access_token=%s')%(access_token)
    cprint('GET request url: %s' % (request_url), 'blue')
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            cprint("Your image has been downloaded.",'green')
            #print "and the post id is:-%s" %(own_media['data'][0]['id'])

            # finding the post with minimum number of likes.
            likes_count = []
            for a in range(0, len(own_media['data'])):
                likes_count.append(own_media['data'][a]['likes']['count'])
            # list.index(max(list))   --- to find the index
            cprint('the url of post with minimum number of likes are:%s'%(own_media['data'][likes_count.index(min(likes_count))]['images']['standard_resolution']['url']),'green')

        else:
            cprint("Post does not Exist.",'green')
    else:
        cprint('Status Code = %s, which is not 200.' % (own_media['meta']['code']),'green')



# Function(d) declaration to get the user's post using insta username.
def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        cprint("User does not exist!",'green')
        start_bot()
    request_url = (base_url + 'users/%s/media/recent/?access_token=%s') %(user_id,access_token)
    cprint('GET request url: %s' % (request_url), 'blue')
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            cprint("Your image has been downloaded.",'green')
            cprint("and the post id is:-%s" %(user_media['data'][0]['id']),'green')

            # finding the post with minimum number of likes.
            likes_count = []
            for a in range(0, len(user_media['data'])):
                likes_count.append(user_media['data'][a]['likes']['count'])
            # list.index(max(list))   --- to find the index
            cprint('the url of post with minimum number of likes are:%s'%(user_media['data'][likes_count.index(min(likes_count))]['images']['standard_resolution']['url']),'green')

        else:
            cprint("Post does not Exist.",'green')
    else:
        cprint('Status Code = %s, which is not 200.' % (user_media['meta']['code']),'green')



# Function(e) declaration to get the recent post liked by self.
def recent_media_liked():
    request_url = (base_url + 'users/self/media/liked?access_token=%s')%(access_token)
    cprint('GET request url: %s' % (request_url), 'blue')
    recent_media = requests.get(request_url).json()

    if recent_media['meta']['code'] == 200:
        if len(recent_media['data']):
            image_name = recent_media['data'][0]['id']
            image_url = recent_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            cprint("The recent media liked by the user is downloaded.",'green')



# Function declaration to get the ID of the recent post of a user by username
def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        cprint("User does not exist!",'green')
        start_bot()

    request_url = (base_url + 'users/%s/media/recent?access_token=%s')%(user_id,access_token)
    cprint('GET request url: %s' % (request_url), 'blue')
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            cprint( 'There is no recent post of the user!','green')
            exit()
    else:
        cprint( 'Status Code = %s, which is not 200.' % (user_media['meta']['code']),'green')
        start_bot()



# Funstion(f) declaration to like the recent post of a user
def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (base_url + 'media/%s/likes')%(media_id)
    payload = {"access_token":access_token}
    cprint('POST request url: %s' % (request_url), 'blue')
    post_a_like = requests.post(request_url,payload).json()
    if post_a_like['meta']['code'] == 200:
        cprint("LIKE was Successful",'green')
    else:
        cprint("Your LIKE was Unsuccessful.Sorry",'green')



# Function(g) declaration to get the list of comments on the post.
def list_of_comments(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (base_url + 'media/%s/comments?access_token=%s')%(media_id, access_token)
    cprint('GET request url: %s' % (request_url), 'blue')
    listing_comments = requests.get(request_url).json()
    if listing_comments['meta']['code'] == 200:
        if listing_comments['data']:
            comments = []
            for c in range(0,len(listing_comments['data'])):
                comments.append(listing_comments['data'][c]['text'])
            cprint("The comments are:\n",'green')
            for b in comments:
                cprint(b,'green')
        else:
            cprint ('No data found','green')
    else:
        cprint( 'Status Code = %s, which is not 200.' % (listing_comments['meta']['code']),'green')
        exit()



# Function(h) declaration to make a comment on the recent post of the user
def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("What do you want to comment:- ")
    payload = {"access_token": access_token, "text": comment_text}
    request_url = (base_url + 'media/%s/comments')%(media_id)
    cprint('POST request url: %s' % (request_url), 'blue')

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        cprint ("The comment has been added!!",'green')
    else:
        cprint( "Unable to add the comment. Sorry!",'green')



# Function(i) comment on the targeted posts
def targeted_comments():
    tag_name = raw_input("Enter the tag you wan to search. ")       # Search for tag udaipur
    request_url = (base_url + 'tags/%s/media/recent?access_token=%s&count=5') % (tag_name, access_token)
    cprint('GET request url: %s' % (request_url), 'blue')
    recent_tag = requests.get(request_url).json()
    media_id = []
    if recent_tag['meta']['code'] == 200:
        if recent_tag['data']:
            for tags in range(0, len(recent_tag['data'])):
                media_id.append(recent_tag['data'][tags]['id'])
            for b in media_id:
                cprint(b,'green')
                comment_text = raw_input("What do you want to comment:- ")        # The comments from any tours and travel company can be added.
                request_urll = (base_url + 'media/%s/comments') % (b)
                cprint('POST request url: %s' % (request_urll), 'blue')
                payload = {"access_token": access_token, "text": comment_text}
                make_comment = requests.post(request_urll, payload).json()
                if make_comment['meta']['code'] == 200:
                    cprint( "The comment has been added",'green')
                else:
                    cprint ("Unable to add a comment. sorry!",'green')
        else:
            cprint("no data found",'green')
    else:
        cprint("code other than 200",'green')

# Now starting the itsinstabot
def start_bot():
    while True:
        print '\n'
        cprint ('Hey! Welcome to itsinstabot','blue')
        cprint ('Here are your menu options:-','blue')
        cprint ('a. Get your own details.\n' \
              'b. Get details of a user by username\n' \
              'c. Get your own recent post\n' \
              'd. Get the recent post of a user by username\n' \
              'e. Get the recent post liked by self\n' \
              'f. Like the recent post of a user\n' \
              'g. Get a list of comments on the recent post of a user\n' \
              'h. Make a comment on the recent post of a user\n' \
              'i. targeted commented on posts of a user\n' \
              'j. Exit','red')
        choice = raw_input("Enter your choice:")
        if choice.lower() == "a":
            self_info()

        elif choice.lower() == 'b':
            insta_username = raw_input("Enter the username of the user:")
            get_user_info(insta_username)
            print 'JSON object could not be decoded.'

        elif choice.lower() == 'c':
            get_own_post()

        elif choice.lower() == 'd':
            insta_username = raw_input("Enter the username of the user:")
            get_user_post(insta_username)

        elif choice.lower() == 'e':
            recent_media_liked()

        elif choice.lower() == "f":
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)

        elif choice.lower() == 'g':
            insta_username = raw_input("Enter the username of the user: ")
            list_of_comments(insta_username)

        elif choice.lower() == "h":
            insta_username = raw_input("Enter the username of the user: ")
            post_a_comment(insta_username)

        elif choice.lower() == 'i':
            targeted_comments()

        elif choice.lower() == "j":
            exit()

        else:
            cprint("WRONG CHOICE",'red')
            cprint("Enter your choice again",'red')
            start_bot()

start_bot()