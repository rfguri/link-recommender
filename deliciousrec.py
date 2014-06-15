# Python imports
import pydelicious,time

# Builds dataset from delicious api
def initialize_user_dict(tag,count=5):
    user_dict={}
    # Get the top "count" popular posts
    for p1 in pydelicious.get_popular(tag=tag)[0:count]:
        # Find all users who posted the same post url
        for p2 in pydelicious.get_urlposts(p1['url']):
            user=p2['user']
            user_dict[user]={}
    return user_dict

# Fills dataset from delicious api
def fill_items(user_dict):
    all_items={}
    # Find links posted by all users
    for user in user_dict:
        for i in range(3):
            try:
                posts=pydelicious.get_userposts(user)
                break;
            except:
                print "Failed to get posts from "+user+", retrying..."
                time.sleep(4)
        for post in posts:
            url=post['url']
            user_dict[user][url]=1.0
            all_items[url]=1
        # Fill in missing items with 0
        for ratings in user_dict.values():
            for item in all_items:
                if item not in ratings:
                    ratings[item]=0.0

