import re
#your code goes here
valide = r"^[1|8|9][0-9]{7}$"
a=input()
res=re.search(valide,a)
if res:
    print("Valid")
else :
    print("Invalid")