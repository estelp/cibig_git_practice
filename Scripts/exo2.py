# Calculate the average of 3 grades

## ask the user to enter 3 grades, which are stored in 3 variables

grade1 = input("Enter your first grade: ")
grade2 = input("Enter your second grade: ")
grade3 = input("Enter your third grade: ")

## convert the values because the 'input' function returns strings

grade1_int = float(grade1)
grade2_int = float(grade2)
grade3_int = float(grade3)

## sum of the 3 grades
somme = grade1_int + grade2_int + grade3_int
print(somme)

## average of the sum

average = somme/3

## print results

print(average)

## print results with 2 decimal

print(f"average is {average:.2f}")

## print results with 3 decimal

print(f"average is {average:.3f}")

## Display results comments

if average < 10:
    print(f"failed! your average is {average:.2f}")
elif average < 12:
    print(f"passable! your average is {average:.2f}")
elif average < 14:
    print(f"fairly good! your average is {average:.2f}")
elif average < 16:
    print(f"good! your average is {average:.2f}")
if average < 20:
    print(f"very good! your average is {average:.2f}")
else:
    print(f"error! your average is > 20")



