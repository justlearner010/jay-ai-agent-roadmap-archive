import sys
import json

fname = sys.argv[1]
chunk_size = int(sys.argv[2])
def text_chunk(fname,chunk_size):
    with open(fname,'r') as f:
        text = f.read()
    chucks = []
    for i in range(0,len(text),chunk_size):
        chunk_data ={"chunk index":i,"chunk_start":i,"chunk_end":i+chunk_size,"chunk_text":text[i:i+chunk_size]}
        chucks.append(chunk_data)
    
    return chucks

j_txt = json.dumps(text_chunk(fname,chunk_size),ensure_ascii=False,indent=4)

def create_json(chunks):
    with open("test.json","w")as f:
        json.dump(
            chunks,
            f,
            ensure_ascii=False,
            indent=4
        )
chunks=text_chunk(fname,chunk_size)

create_json(chunks)

print("JSON file created successfully")



