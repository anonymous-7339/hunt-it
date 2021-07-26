  
import time, datetime, os, sys 
x = datetime.datetime.now()
os.system("clear")


print(" _                 _          _ _    ")
print("| |               | |        (_) |   ")
print("| |__  _   _ _ __ | |_ ______ _| |_  ")
print("| '_ \| | | | '_ \| __|______| | __| ")
print("| | | | |_| | | | | |_       | | |_  ")
print("|_| |_|\__,_|_| |_|\__|      |_|\__| ")
print()                                                                 	 	
print("No technology that's connected to the internet is unhackable ")
print("\033[94m Hunt-it is an OSINT tool to extract information from any Google Account using an email.\033[94m")             
print()
print("\033[92m author by krishna/7339")
print(" Twitter:  https://twitter.com/KRISHNA_NANDIVELUGU ")
print(" Insta :  https://instagram.com/krishna_7339_ \033[0m")
print(" Do what you love , love what you do ")
print()
regexs = {
    "albums": r'href=\"\.\/albumarchive\/\d*?\/album\/(.*?)\" jsaction.*?>(?:<.*?>){5}(.*?)<\/div><.*?>(\d*?) ',
    "photos": r'\],\"(https:\/\/lh\d\.googleusercontent\.com\/.*?)\",\[\"\d{21}\"(?:.*?,){16}\"(.*?)\"',
    "review_loc_by_id": r'{}\",.*?\[\[null,null,(.*?),(.*?)\]'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Connection': 'Keep-Alive'
}

headless         = True # if True, it doesn't show the browser while scraping GMaps reviews
ytb_hunt_always  = True # if True, search the Youtube channel everytime
gmaps_radius     = 30 # in km. The radius distance to create groups of gmaps reviews.
gdocs_public_doc = "1jaEEHZL32t1RUN5WuZEnFpqiEPf_APYKrRBG9LhLdvE"  # The public Google Doc to use it as an endpoint, to use Google's Search.
data_path        = "resources/data.txt"

# Profile pictures options
write_profile_pic = True
profile_pics_dir = "profile_pics"

# Cookies
# if True, it will uses the Google Account cookies to request the services,
# and gonna be able to read your personal informations
gmaps_cookies = False
calendar_cookies = False
default_consent_cookie = "YES+FR.fr+V10+BX"