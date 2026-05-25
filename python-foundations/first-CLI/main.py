import argparse

from word_freq import word_freq_cnt
from word_chunk import text_chunk
from create_json import create_json
from text_status import line_check
from text_status import space_check
from text_status import word_check
from text_status import digit_check

parser = argparse.ArgumentParser()

parser.add_argument("filename")
parser.add_argument("--chunk_size",type=int,default=500)
args = parser.parse_args()


#传入文件名、词块大小
fname = args.filename
chunk_size = args.chunk_size

chunks=text_chunk(fname,chunk_size)
create_json(chunks)
print("Successfully create the json")

freq_result = word_freq_cnt(fname)
print("Top 10 words in this text!")
print(freq_result)

lines = line_check(fname)
print(f"行数为{lines}行")

words = word_check(fname)

print(f"单词数为{words}个单词")

space= space_check(fname)
print(f"空格数为{space}")

digit = digit_check(fname)

print(f"数字的个数为{digit}")

