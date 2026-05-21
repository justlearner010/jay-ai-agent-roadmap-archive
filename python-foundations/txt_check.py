fname = input("filename")
fo = open(fname,"r")
read_line = 0
w_cnt = 0
digit_cnt = 0
total_cnt = 0
for line in fo.readlines():
    read_line= read_line+1 
    for word in line:
        if(word ==" "):
            w_cnt = w_cnt + 1
        if(word >="1" and word <="9"):
            digit_cnt = digit_cnt+1
        if(word !=" "):
            total_cnt = total_cnt + 1
fo.close()

print("文件的行数为",read_line,"行")
print("文件的数字的数量为",digit_cnt)
print("文件的单词为",w_cnt+1)
print("文件的总字符数为",total_cnt)
