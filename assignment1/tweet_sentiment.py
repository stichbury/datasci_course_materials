import sys
import json

def dictbuild():
    afinn_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinn_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    
    tweet_file = open(sys.argv[2])


    for line in tweet_file:
        tweet = json.loads(line)
        sentscore=0
        if 'lang' in tweet.keys() and tweet["lang"]=='en': 
            if 'text' in tweet.keys():    
                #print tweet["text"]
                tweetwords = tweet["text"].split()
                for word in tweetwords:
                    if word in scores:
                        sentscore+=scores[word]

        print sentscore                

def main():
    
    dictbuild()

if __name__ == '__main__':
    main()
