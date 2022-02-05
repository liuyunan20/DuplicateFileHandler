# put your python code here
sum_ = 0
square_sum = 0
while True:
    a = int(input())
    sum_ += a
    square_sum += a ** 2
    if sum_ == 0:
        print(square_sum)
        break
