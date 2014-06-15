# Library imports
import recommendations, deliciousrec

# Initialize delicious users
delusers=deliciousrec.initialize_user_dict('programming')
# Add myself to the dataset
delusers['rogerfernandezg']={}
# Fills delicious users with data from delicious
deliciousrec.fill_items(delusers)
# Show recommendations for specific user
user=delusers.keys()[1]
print recommendations.top_matches(delusers,user)[0:10]
url=recommendations.get_recommendations(delusers,user)[0][1]
print recommendations.top_matches(recommendations.transform_prefs(delusers),url)
