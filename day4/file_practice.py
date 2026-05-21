# Write
file=open("sample.txt","w")
file.write("Hello Python\n")
file.close()

# Read
file=open("sample.txt","r")
print(file.read())
file.close()

# Append
file=open("sample.txt","a")
file.write("Learning File Handling")
file.close()