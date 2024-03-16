ch=input("Enter the character")
if(ch.islower()):
    print(ch,"is a lower case")
elif(ch.isupper()):
    print(ch,"is upper case ")
elif(ord(ch)>=48 and ord(ch)<=57):
    print(ch,"is a digit")
else:
    print(ch,"is special character")