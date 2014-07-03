import oauth2 as oauth
import urllib2 as urllib

# See assignment1.html instructions or README for how to get these credentials

api_key = "sHceQ95QAWEC1bHkU04CehgoW"
api_secret = "A8rLiPQ39AVSj1rqu2Ls4bqG37AxDFG1mnAnROhpimrA50fXzb"
access_token_key = "5355212-JA4CTaHAKzWlGrZc4Md8lS9eGozqA8ouQ6X0FQPfSv"
access_token_secret = "JyKJAcNOSWlairf6KFLrlBdMQWVSX8AJdXKokWk7x3v8m"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()

if __name__ == '__main__':
  fetchsamples()
