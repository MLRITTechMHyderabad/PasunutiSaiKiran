groupOfWords="This will open a new tab in your default web browser. You should see the Jupyter Notebook dashboard, which is essentially a file"

count={}
for word in groupOfWords.split(" "):
    count[word]=count.get(word,0)+1
print(count)