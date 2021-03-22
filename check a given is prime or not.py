#Write a program to check whether a  given no.is prime or not ...

x=int(input("enter your desired no."))
if x%1==0 and x%2!=0 and x%3!=0:
    print("it is prime")
else:
    print("not prime")
