import argparse
import sys

from word_freq import word_freq_cnt
from word_chunk import Wordchunk
from create_json import create_json
from text_status import TextStats

parser = argparse.ArgumentParser()

parser.add_argument("filename")
parser.add_argument("--chunk_size", type=int, default=500)
args = parser.parse_args()




# 传入文件名、词块大小
fname = args.filename
chunk_size = args.chunk_size

try:
    with open(fname) as f:
        print(0)        
except FileNotFoundError:
    sys.exit("File does not found")


stats = TextStats(fname)



chunk1 = Wordchunk(fname,chunk_size)

chunks = chunk1.text_chunk()

create_json(chunks)#输出json文件
print("Successfully create the json")

freq_result = word_freq_cnt(fname)
print("Top 10 words in this text!")
print(freq_result)#打印词频最高的十个单词

lines = stats.line_check()
print(f"行数为{lines}行")#打印行

words = stats.word_check()

print(f"单词数为{words}个单词")#打印单词数

space = stats.space_check()
print(f"空格数为{space}")#打印空格数

digit = stats.digit_check()

print(f"数字的个数为{digit}")#打印数字数
