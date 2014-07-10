import sys
import json
import operator

#remove duplicates from a list  
def f7(seq):  
   seen = set()  
   seen_add = seen.add  
   return [ x for x in seq if x not in seen and not seen_add(x)]  

def gogogo():
    
    tweet_file = open(sys.argv[1])
    tagsdict = {} # Empty dictionary to hold all terms
    allwordscount = 0
    
    for line in tweet_file:
        tweet = json.loads(line)
        
        if 'entities' in tweet.keys() and tweet["entities"]["hashtags"] != []:  
            for hashtag in tweet["entities"]["hashtags"]:
                if hashtag["text"] in tagsdict.keys() : # Already in the nondictionary set
                    tagsdict[hashtag["text"]] += 1
                else :    
                    tagsdict[hashtag["text"]] = 1



    
    sortedDict = sorted(tagsdict.iteritems(), key=operator.itemgetter(1), reverse=True)
    for i in range(10):
        hashtag, value= sortedDict[i]
        listing = hashtag+' '+str(value)
        encoded_listing = listing.encode('utf-8')
        print encoded_listing              

    



def main():
    gogogo()

if __name__ == '__main__':
    main()
