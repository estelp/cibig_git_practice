# Calculate the average of 3 grades

## ask the user to enter 3 grades, which are stored in 3 variables and
## convert the values because the 'input' function returns strings

grade1 = float(input("Enter your first grade: "))
grade2 = float(input("Enter your second grade: "))
grade3 = float(input("Enter your third grade: "))

## calculate average

average = (grade1 + grade2 + grade3)/3

## print results

print(average)

## print results with 2 decimal

print(f"average is {average:.2f}")

## print results with 3 decimal

print(f"average is {average:.3f}")

## Display results comments

### display "very good" if the average is greater than or equal to 16
if average > 20:
    print(f"error! your average is > 20")
elif 16 <= average < 20:
    print(f"very good! your average is {average:.2f}")
### display "good" if the average is greater than or equal to 14
elif 14 <= average < 16:
    print(f"good! your average is {average:.2f}")
### display "fairly good" if the average is greater than or equal to 12
elif 12 <= average < 14:
    print(f"fairly good! your average is {average:.2f}")
### display "passable" if the average is greater than or equal to 10
elif 10 <= average < 12:
    print(f"passable! your average is {average:.2f}")
### display "failed" if the average is less than 10
else:
    print(f"failed! your average is {average:.2f}")
