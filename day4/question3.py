def multiply(lst):
    result=1

    for i in lst:
        result*=i

    return result

numbers=[2,3,4,5]

print("Multiplication:",multiply(numbers))