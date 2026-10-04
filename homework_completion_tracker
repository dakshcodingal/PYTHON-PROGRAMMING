#My chore checklist countdown

#Part 1:Set today"s total number of chores(no list needed)
Total_chores=4
original_count=Total_chores
print(f"You have {original_count} chores to finish today!\n")

#part 2:Keep a counter for completed chores and the current chore number
completed_count=0
chore_num=1

# part 3:Repeat while there are still chores left to check off
while chore_num <= Total_chores:


    if chore_num == 1: next_chore= "Make your bed"
    elif chore_num == 2: next_chore= "Feed the pet"
    elif chore_num == 3: next_chore= "Take out the trash"
    else: next_chore = "Wash the dishes"

    answer=input(f"Have you finished: {next_chore}?(yes/no):")


    if answer == "yes":
        completed_count+=1
        chore_num+=1
        print("Great job! chore completed.")
    else:
        print("okay, finish it and check again!")


        print("chores remaining:", total_chores - completed_count)
        print()


print("===== All chores complete! =====")
print("Great work finishing your entire checklist today!\n")


print("Now let's safely peak at an infinite loop... ")
test_value=0
safety_counter=0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter +=1
    if safety_counter ==3:
        print("(stopping here on purpose - a real infinite loop never stops on it's own!)")
        break


print("\n==== Chore checklist summary ====")
print("Chores assigned today:", original_count)
print("Chores completed:", completed_count)
print("Chores remaining:", Total_chores - completed_count)
print("/////////////")