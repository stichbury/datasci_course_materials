import sys
import json

#remove duplicates from a list  
def f7(seq):  
   seen = set()  
   seen_add = seen.add  
   return [ x for x in seq if x not in seen and not seen_add(x)]  

def sentiment():
    afinn_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinn_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    
    nondictionarywords = {} # Another empty dictionary to hold non-dictionary words
    tweet_file = open(sys.argv[2])

    for line in tweet_file:
        tweet = json.loads(line)
        sentscore=0
        if 'lang' in tweet.keys() and tweet["lang"]=='en':  # It's in English
            if 'text' in tweet.keys():  # There's some tweet text  
                tweetwords = tweet["text"].split()
                for word in tweetwords: 
                    if word in scores: # There's a word in the sentiment dictionary
                        sentscore+=scores[word]
                           
                        
                if sentscore != 0 :                 # This is where we can pick up  sentimental tweets
                    sentscore+=0.0                  # Make it into a float
                    uniquewords = f7(tweetwords)    # Build a list of all words in the tweet
                    for word in uniquewords :       # Run through unique words
                        if word not in scores:      # A non-dictionary word
                            encoded_word = word.encode('utf-8')
                            if encoded_word in nondictionarywords.keys() : # Already in the nondictionary set
                                nondictionarywords[encoded_word] += (sentscore/len(tweetwords))
                            else :    
                                nondictionarywords[encoded_word] = (sentscore/len(tweetwords))



    
    for word in nondictionarywords:  
         listing = word+' '+str(nondictionarywords[word])  
         print listing               

    # For each tweet that contains sentiment:
    # Make a set of unique words in the tweet that *aren't* in the dictionary                
    # Assign each a score according to the sentiment in the tweet
    # Add to the collection of total words   




def main():
    sentiment()

if __name__ == '__main__':
    main()
