#This program prints stars in pyramid shape.
num= int(input("Enter number of rows:"))

row = 0
while row<num:
    space = num-row-1
    while space>0:
        print(end=" ")
        space = space-1

    star = row+1
    while star>0:
        print("*",end=" ")
        star = star-1
    row = row+1
    print()

"""
OUTPUT:
Enter number of rows:5
    *
   * *
  * * *
 * * * *
* * * * *

"""