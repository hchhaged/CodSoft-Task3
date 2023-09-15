import string
import random
print("-------------------------WELCOME TO PASSWORD GENERATOR-----------------------\n")
def main():
    s1=string.ascii_lowercase
    #print(s1)
    s2=string.ascii_uppercase
    #print(s2)
    s3=string.digits
    #print(s3)
    s4=string.punctuation
    #print(s4)
    plen=int(input("Enter the desired password length: "))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    a=("".join(s[0:plen]))
    print("Your desired password is: ",a,"\n")
    main()
main()
