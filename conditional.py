print("==========smart school day planner============")
day = input("what day is it today? (monday-sunday): ").strip().lower()
weather = input("what is the weather? (sunny-cloudy-rainy): ").strip().lower()
homework = input("is homework done?: ").strip().lower()

print("**********Your plan for the day ",day, "*********")
if day in ("saturday", "sunday"):
    print("day type:weekend")
elif day =="monday":
    print("day type :first day of week")
elif day=="friday" :
    print("day type :last day of week")
elif day in ("tuesday","wednesday","thursday"):
    print("regular days of the week")
if weather =="sunny" and homework =="yes" :
    print("you can go and play")
if weather == "rainy" or weather == "cloudy" :
    print("you need to take umbrella")

