# 2. Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.


def check(a):
    if len(a)==0 or a[0]!=a[-1]:
        return False
    
    else:
        return True
    

a=[1]

r=check(a)
print("The condition that first and last number of a given list is same is {0} ".format(r))
    
