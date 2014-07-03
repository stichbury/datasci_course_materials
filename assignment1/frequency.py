import sys
import json

#remove duplicates from a list  
def f7(seq):  
   seen = set()  
   seen_add = seen.add  
   return [ x for x in seq if x not in seen and not seen_add(x)]  

def gogogo():
    
    tweet_file = open(sys.argv[1])
    termsdict = {} # Empty dictionary to hold all terms
    allwordscount = 0
    
    for line in tweet_file:
        tweet = json.loads(line)
        
        if 'lang' in tweet.keys() and tweet["lang"]=='en':  # It's in English
            if 'text' in tweet.keys():  # There's some tweet text  
                tweetwords = tweet["text"].split()
                allwordscount+=len(tweetwords)
                uniquewords = f7(tweetwords)    # Build a list of all unique words in the tweet
        
                for word in uniquewords :       # Run through unique words and add to larger set
                    if word in termsdict.keys() : # Already in the nondictionary set
                        termsdict[word] += 1
                    else :    
                        termsdict[word] = 1



    
    for word in termsdict: 
        termsdict[word]+=0.0
        termsdict[word]/=allwordscount
        listing = word+' '+str(termsdict[word])  
        encoded_listing = listing.encode('utf-8')
        print encoded_listing               

    # For each tweet that contains sentiment:
    # Make a set of unique words in the tweet that *aren't* in the dictionary                
    # Assign each a score according to the sentiment in the tweet
    # Add to the collection of total words   




def main():
    gogogo()

if __name__ == '__main__':
    main()
