print(" ")
fibonacci_nums = [1, 2]
ii = -1
answer = 0
while True:
    ii += 1
    qn = fibonacci_nums[ii] + fibonacci_nums[ii + 1]
    if qn < 4000000:  # здесь может быть другое число
        print(qn)
        fibonacci_nums.append(qn)
    else:
        break
print(" ")
for a in fibonacci_nums:
    if round(a / 2) == a / 2:
        print(a)
        answer += a
print(" ")
print(answer)