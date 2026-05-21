def count_case(text):

    upper=0
    lower=0

    for i in text:
        if i.isupper():
            upper+=1

        elif i.islower():
            lower+=1

    print("Upper case:",upper)
    print("Lower case:",lower)

string=input("Enter string: ")

count_case(string)
