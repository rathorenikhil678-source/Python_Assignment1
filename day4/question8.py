def prime(num):

    if num<=1:
        return False

    for i in range(2,num):
        if num%i==0:
            return False

    return True

number=int(input("Enter number: "))

if prime(number):
    print("Prime Number")
else:
    print("Not Prime")