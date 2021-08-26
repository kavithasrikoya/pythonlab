string=input("enter string:")
sub_str=input("enter word:")
if(string.find(sub_str)==-1):
    print("substring not found in string!")
else:
    print("substring in string!")
