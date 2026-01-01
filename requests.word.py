#import requests

#words = input("Enter the word:")
#res = requests.get(f"https://api.datamuse.com/words?sl={words}")
#data = res.json()

#for word in data:
 #   print(word['word'])

import requests
#text=input("enter a text")
res=requests.get(f"https://api.datamuse.com/words?sl=Archana")

data=res.json()
for word in data:
    print(word['word'])