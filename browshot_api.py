
import hmac
import hashlib
import urllib
 
 
def screenshotlayer(access_key, secret_keyword, url, args):
    
    # encode URL
    query = urllib.urlencode(dict(url=url, **args))
 
    # generate md5 secret key
    secret_key = hashlib.md5('{}{}'.format(url, secret_keyword)).hexdigest()
 
    return "https://api.screenshotlayer.com/api/capture?access_key=%s&secret_key=%s&%s" % (access_key, secret_key, query)

# set optional parameters (leave blank if unused)
params = {
    'fullpage': '',
    'width': '',
    'viewport': '',
    'format': '',
    'css_url': '',
    'delay': '',
    'ttl': '',
    'force': '',
    'placeholder': '',
    'user_agent': '',
    'accept_lang': '',
    'export': ''
};
 
# set your access key, secret keyword and target URL 
access_key = "aa1626836d09ccf550107705e5ae6c35"
secret_keyword = "YOUR_SECRET_KEYWORD"
url = "www.cnn.com"
 
print(screenshotlayer (access_key, secret_keyword, url, params))
