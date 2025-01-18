First = int(input("Enter the starting number of the range: "))
Last = int(input("Enter the ending number of the range: "))

if First > Last:
    print("invalid range!")
else:
    Numbers = [i ** 2 for i in range(First, Last + 1)]
    print(Numbers)