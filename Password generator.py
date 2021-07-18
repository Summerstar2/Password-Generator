import random
import array
def Continue():
    Again=str(input("Would you like to use this program again? (Yes/No) "))
    if Again=="No":
        return False
    return True
Alphabet_Upper=["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Alphabet_Lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
Numbers=["1","2","3","4","5","6","7","8","9","0"]
Symbols=["!","@","#","$","%","^","&","*","(",")","_","-","+","=","~","`","{","}","[","]","|"]
Main=Alphabet_Upper+Alphabet_Lower+Numbers+Symbols
Digit=random.choice(Numbers)
Lower=random.choice(Alphabet_Lower)
Upper=random.choice(Alphabet_Upper)
Symbol=random.choice(Symbols)
Pass=Digit+Lower+Upper+Symbol
print ("This program will generate a random but strong password for you and store it safely in a file.")
Use=str(input("Do you want to use this program? (Yes/No) "))
if Use=="No":
    quit()
if Use=="Yes":
    print ("To generate a safe and strong password there are a few parameters.")
    print ("This program is very customizable so you can choose what sorts of numbers, alphabets and symbols go into it.")
    Characters=int(input("Enter the number of characters in the password - "))
    Name=str(input("Enter the username or email this password is attached to - "))
    for x in range (Characters):
        Pass= Pass+ random.choice(Main)
        PassList=array.array('u',Pass)
        random.shuffle(PassList)
    Password=""
    for x in PassList:
        Password=Password+x
    print ("Your randomly generated password is ",Password)