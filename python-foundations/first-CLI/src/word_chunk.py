
# 用argparse改写的新版本

def text_chunk(fname,chunk_size):
    if(chunk_size < 0):
        print("你的文本块大小无效")
        return -1
    with open(fname,'r') as f:
        text = f.read()
    chunks = []
    j = 0
    for i in range(0,len(text),chunk_size):
        j = j+1
        chunk_data ={"chunk index":j,
                     "chunk_start":i,
                     "chunk_end":min(i+chunk_size,len(text)),
                     "chunk_text":text[i:i+chunk_size]
                     }
        chunks.append(chunk_data)
    
    return chunks












