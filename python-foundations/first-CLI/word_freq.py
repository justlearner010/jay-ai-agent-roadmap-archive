from collections import Counter

# fname = input("filename")
# word_cnt ={}
# def word_freq_cnt(fname):
#     with open(fname,"r") as f:
#         for line in f:
#             words = line.strip().split()
#             for word in words:
#                 word = word.lower()
#                 if word in word_cnt:
#                     word_cnt[word] += 1

#                 else:
#                     word_cnt [word] = 1
#     for word, count in list(word_cnt.items())[:10]:
#         print(word, count)
# word_freq_cnt(fname)


#dict版本
# def word_freq_cnt1(fname):
#     word_cnt ={}
#     with open(fname,'r') as f:
#         for line in f:
#             words = line.strip().split()
#             for word in words:
#                 word = word.lower()
#                 if(word in word_cnt):
#                     word_cnt[word] +=1
#                 else:
#                     word_cnt[word] = 1
#     top_10_words = [k for k,v in sorted(word_cnt.items(),key = lambda item:item[1],reverse=True)[:10]]
#     print(top_10_words)

    
# collection counter版本

def word_freq_cnt(fname, top_n=10):
    with open(fname, 'r') as f:

        words = [word.lower() for line in f for word in line.strip().split()]
    
    
    counter = Counter(words)
    
    top_words = counter.most_common(top_n)
    
    return top_words


