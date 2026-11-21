filename = "sample.txt"
 
with open(filename, "r") as f:
    text = f.read()
 
words = text.split()
print("Number of words     :", len(words))
print("Number of lines     :", len(text.splitlines()))
print("Number of characters:", len(text))
 
# Count of each word
count = {}
for w in words:
    w = w.lower().strip(".,!?")
    count[w] = count.get(w, 0) + 1
 
print("Word frequency:")
for w, c in count.items():
    print(w, ":", c)
