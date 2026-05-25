#5.21作业第一版

#fname = input("filename")
#fo = open(fname,"r")
#read_line = 0
#w_cnt = 0
#digit_cnt = 0
#total_cnt = 0
#for line in fo.readlines():
#    read_line= read_line+1 
#    for word in line:
#        if(word ==" "):
#            w_cnt = w_cnt + 1
#        if(word >="1" and word <="9"):
#            digit_cnt = digit_cnt+1
#        if(word !=" "):
#            total_cnt = total_cnt + 1
#fo.close()

#print("文件的行数为",read_line,"行")
#print("文件的数字的数量为",digit_cnt)
#print("文件的单词为",w_cnt+1)
#print("文件的总字符数为",total_cnt)


#5.21作业第二版 :已实现函数化

def line_check(fname):
    lines = 0
    with open(fname,"r") as file:
        for line in file:
            lines = lines+1

    return lines



def word_check(fname):
    word_cnt = 0
    with open(fname,"r") as file:
        for line in file:
            words = line.split()
            word_cnt +=len(words)
    return word_cnt

def digit_check(fname):
    digit_cnt = 0
    with open(fname,"r") as f:
        for line in f:
            for word in line:
                if(word.isdigit()):
                    digit_cnt += 1
    return digit_cnt

def space_check(fname):
    space_cnt = 0
    with open(fname,"r") as f:
        for line in f:
            for word in line:
                if(word.isspace()):
                    space_cnt += 1
    return space_cnt


