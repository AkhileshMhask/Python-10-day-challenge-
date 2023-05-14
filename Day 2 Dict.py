#Dictonary 

d = {
    "When did India gain independence?":"1949",
    "When did India win the first cricket cup?":"1978",
    "When was DY Patil found?": "1945"
}
score=0
for i in d:
    print(i)
    ans = input ("Your answer: ")
    if ans == d[i]:
        score+=1
print(score)
 