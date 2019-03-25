answer = 0

for i in range(1000):
    if i / 3 == round(i / 3) or i / 5 == round(i / 5):
        print(i)
        answer += i
print(" ")
print(answer )