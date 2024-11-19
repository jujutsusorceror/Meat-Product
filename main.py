num = int(input("Enter the number"))
temp = num
num_len = 0

while temp> 0:
    num_len += 1
    temp = temp // 10
print("The digit of the number", num_len)

if num_len < 4 :
    print("Please enter a number that has more than 3 digits")
else :
    num_len = num_len // 2
    check = 0
    while num > 0:
        rem = num % 10 
        if check == num_len:
            mid_one = rem
        elif check == (num_len -1):
            mid_two = rem
        num = num // 10
        check += 1
    prod = mid_one * mid_two
    print(f"The product of {mid_one} and {mid_two} is {prod}")       