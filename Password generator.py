import random
import array
def Generate_new():
    Again=str(input("Would you like to generate a new password? (Yes/No) "))
    if Again=="No":
        return False
    return True
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
while True:
    Open=str(input("Do you want to read the current passwords or generate and write new ones? (Read/Write) "))
    if Open=="Read":
        Masterpassword=str(input("Enter the master password - "))
        if Masterpassword=="Sample":       #You can enter whatever master password you want for the file.
            with open ("Passwords.txt","r") as R:
                print (R.read())
        if Masterpassword!="Sample":
            Attempts=0
            Threshold=2
            while Attempts<Threshold:
                print ("Invalid password given.")
                Attempts+=1
                Masterpassword=str(input("Enter the master password - "))
                if Attempts==Threshold:
                    print ("Too many attempts, program quit.")     #Program automatically quits after 3 attempts to give the master password.
                    quit()
        with open ("Passwords.txt","r") as R:
            print (R.read())
    if Open=="Write":
        with open ("Passwords.txt","a") as W:
            while True:
                Characters=int(input("Enter the number of characters in the password - "))
                Name=str(input("Enter the username or email this password is attached to - "))
                for x in range (Characters):
                    Pass= Pass+ random.choice(Main)
                    PassList=array.array('u',Pass)
                    random.shuffle(PassList)
                Password=""
                for x in PassList:
                    Password=Password+x
                W.write(Name + " | " + Password + "\n")
                print ("This password and name is now stored into the file.")
                print ("To read these passwords you have to enter the master password under the Read choice.")
                if not Generate_new():
                    break
    if not Continue():
        break
