words = ['donkey', 'fuck','bitch','shit']
with open("another.txt","r") as f:
    data = f.read()
    for word in words:      # This one is importatnt to find whether word is present in your text file or not
        data = data.replace( word,'#%$**%$')
        with open("another.txt","w") as f:
            f.write(data)
