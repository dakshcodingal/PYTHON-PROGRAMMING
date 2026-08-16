temperature = int(input("enter temperature "))
if temperature < 20 :
    outfit="jacket"
    print("its too cold outside. wear ",outfit)
else :
    outfit ="tshirt"
    print("its warm outside, wear",outfit)
is_raining = input("is it raining (yes/no) ")
if is_raining == "yes" :
    print("take umbrella with you.")
has_puddles= input("Are there puddles? (yes/no): ")
if has_puddles == "yes":
    shoes = "boots"
    print("wear ", shoes)
else :
    shoes="sneakers"
    print("the ground is dry",  shoes)

