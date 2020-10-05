punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(s):
    for c in punctuation_chars:
        snew=s.replace(c,'')
        s=snew
    return s
# list of positive words to use
positive_words = []
with open("/Users/pathikshah/Documents/Python3.8/Sentiment_analysis/positive_words.txt") as pos_f:
    for lin in pos_f:
       if lin[0] != ';' and lin[0] != '\n':
        positive_words.append(lin.strip())

def get_pos(s1):
    count = 0    
    for w in s1.lower().split():
        if strip_punctuation(w) in positive_words:
            count+=1
    return count
negative_words = []
with open("/Users/pathikshah/Documents/Python3.8/Sentiment_analysis/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(s1):
    count = 0    
    for w in s1.lower().split():
        if strip_punctuation(w) in negative_words:
            count+=1
    return count

with open ('/Users/pathikshah/Documents/Python3.8/Sentiment_analysis/project_twitter_data.csv','r') as tw:
    with open ('/Users/pathikshah/Documents/Python3.8/Sentiment_analysis/resulting_data.csv','w') as result:
        fieldnames="Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n"
        l=0
        result.write(fieldnames)
        for line in tw:
            if l==0:
                l+=1
                continue     
            else: 
                l2=line.split(',')
                l3=[l2[1],l2[2].rstrip(),str(get_pos(l2[0])),str(get_neg(l2[0])),str(get_pos(l2[0])-get_neg(l2[0]))]
                result.write(','.join(l3)+'\n')