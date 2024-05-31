T = int(input())
text = []
for _ in range(T):
    text.append(input())

text= set(text)
text = list(text)
text.sort()
text.sort(key=len)

for i in text :
    print(i)