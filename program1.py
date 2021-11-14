# grade/mark    percentage     description
# 1.0           97-100          Excellent
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.50          79-81           Satisfactory
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropped

#Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
def getGradePercentage():
    _gradepercentage = float(input("Input grade:"))
    return _gradepercentage

#other functions
def getIncomplete():
    _incomplete = int(input("Is the student incomplete? Type '1' if yes and '0' if not."))
    return _incomplete

def getWithdrawn():
    _withdrawn = int(input("Is the student withdrawn?, Type '1' if yes and '0' if not."))
    return _withdrawn

def getDropped():
    _dropped = int(input("Is the student dropped out?, Type '1' if yes and '0' if not."))
    return _dropped


# aask kung ang student ba ay incomplete, withdrawn, dropout
incomplete = getIncomplete ()
if incomplete == 1:
    print("Input grade: n/a")
    print("Grade/Mark: Inc.")
    print("Description: Incomplete")
else:
    withdrawn = getWithdrawn ()
    if incomplete == 0 and withdrawn == 1:
        print("Input grade: n/a")
        print("Grade/Mark: W")
        print("Description: Withdrawn")
    else:
        dropped = getDropped ()
        if withdrawn == 0 and dropped == 1:
            print("Input grade: n/a")
            print("Grade/Mark: D")
            print("Description: Dropped")
        else:
            gPercent = getGradePercentage()

#Example:
#Input grade: 87.6
#Grade/Mark: 1.75
#Description: Very Good