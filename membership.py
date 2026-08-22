print("enter marks for following subjects")
english=int(input("english "))
math=int(input("math "))
geo=int(input("geo "))
art=int(input("art "))
science=int(input("science "))
total=english+math+geo+art+science
average=int(total/5)
validRange=range(0,101)
if average not in validRange:
    print("invalid input")
elif average in range(91, 101):
    print("outstanding")
elif average in range(75, 90):
    print("distinction")
elif average in range (50, 75):
    print("first class")