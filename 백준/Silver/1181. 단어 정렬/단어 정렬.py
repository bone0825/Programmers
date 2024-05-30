# 64 32 16 8 4 2 1
T = int(input())
text = []
for _ in range(T):
    text.append(input())

text= set(text)
text = list(text)
text.sort(key= str.lower)
text.sort(key=len)

for i in text :
    print(i)