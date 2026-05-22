fname = input("filename")
word_cnt ={}
def word_freq_cnt(fname):
    with open(fname,"r") as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                word = word.lower()
                if word in word_cnt:
                    word_cnt[word] += 1

                else:
                    word_cnt [word] = 1
    for word, count in list(word_cnt.items())[:10]:
        print(word, count)
word_freq_cnt(fname)
