# 5. Write a program to get roll numbers, names and marks of the students of a class (get from user) and store these details in a file called “Marks.data”

def writeF(r,n,m):

    with open("Marks.data","w") as file:
        file.write(f'{r},{n},{m}')

r=input("Entr the roll No. : ")
n=input("Entr the name: ")
m=input("Entr the marks : ")
writeF(r,n,m)
