# Holiday Activity Planner
# Lesson: Nested Conditional Statements
 
print("====================================")
print("    Welcome to Holiday Planner!     ")
print("====================================")
print()
 
print("Step 1: Pick your holiday type")
print("  1 - Beach Holiday")
print("  2 - Mountain Holiday")
print()
 
choice = int(input("Enter 1 or 2: "))
print()
 
if choice == 1:
    # Nested if-else - runs only when choice is 1
    print("Step 2: Pick your beach activity")
    print("  1 - Jetski")
    print("  2 - Beach ball")
    print()
 
    beach_activity = int(input("Enter 1 or 2: "))
    print()
 
    if beach_activity == 1:
        print("You picked  : Jetski")
        print("Best time   : Morning")
        print("Remember    : Carry sunscreen and water")
    else:
        print("You picked  : Beach ball")
        print("Best time   : Evening")
        print("Remember    : Carry a ball")
 
elif choice == 2:
    # Nested if-else - runs only when choice is 2
    print("Step 2: Pick your mountain activity")
    print("  1 - Biking")
    print("  2 - Camping")
    print()
 
    mountain_activity = int(input("Enter 1 or 2: "))
    print()
 
    if mountain_activity == 1:
        print("You picked  : biking")
        print("Best for    : Off road trials")
        print("Remember    : Wear a fitting helmet")
    else:
        print("You picked  : Camping")
        print("Best for    : Staying close to nature")
        print("Remember    : Carry a tent and flashlight")
 
else:
    print("That was not a valid choice.")
    print("Please enter 1 for Beach Holiday or 2 for Mountain Holiday.")
 
    print()
    print("====================================")
    print("   Your holiday plan is ready!      ")
    print("   Enjoy your trip!                 ")
    print("====================================")
