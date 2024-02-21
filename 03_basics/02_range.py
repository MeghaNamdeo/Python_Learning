# Practice question: WAP to find the sum of the first n numbers using while

i = 1
n = int(input("Enter the value of n: "))
Sum = 0

while i < n:
    Sum = Sum + i
    i = i + 1

print("Sum of the first", n, "numbers:", Sum)
