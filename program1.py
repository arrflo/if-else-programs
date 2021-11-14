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
    _incomplete = int(input("Is the student incomplete? Type '1' if yes and '0' if not:"))
    return _incomplete

def getWithdrawn():
    _withdrawn = int(input("Is the student withdrawn? Type '1' if yes and '0' if not:"))
    return _withdrawn

def getDropped():
    _dropped = int(input("Is the student dropped out? Type '1' if yes and '0' if not:"))
    return _dropped


# aask kung ang student ba ay incomplete, withdrawn, dropout
incomplete = getIncomplete ()
if incomplete == 1:
    print("Grade/Mark: Inc.")
    print("Description: Incomplete")
else:
    withdrawn = getWithdrawn ()
    if incomplete == 0 and withdrawn == 1:
        print("Grade/Mark: W")
        print("Description: Withdrawn")
    else:
        dropped = getDropped ()
        if withdrawn == 0 and dropped == 1:
            print("Grade/Mark: D")
            print("Description: Dropped")
        else:
            gPercent = getGradePercentage()         #start ng input ng grade
            rdgpercent = round(gPercent)
            if dropped == 0  and rdgpercent >= 97 and rdgpercent <= 100:
                print("Grade/Mark: 1.0")
                print("Description: Excellent")
            elif rdgpercent >= 94 and rdgpercent <= 96:
                print("Grade/Mark: 1.25")
                print("Description: Excellent")
            elif rdgpercent >= 91 and rdgpercent <= 93:
                print("Grade/Mark: 1.5")
                print("Description: Very Good")
            elif rdgpercent >= 88 and rdgpercent <= 90:
                print("Grade/Mark: 1.75")
                print("Description: Very Good")
            elif rdgpercent >= 85 and rdgpercent <= 87:
                print("Grade/Mark: 2.0")
                print("Description: Good")
            elif rdgpercent >= 82 and rdgpercent <= 84:
                print("Grade/Mark: 2.25")
                print("Description: Good")
            elif rdgpercent >= 79 and rdgpercent <= 81:
                print("Grade/Mark: 2.5")
                print("Description: Satisfactory")
            elif rdgpercent >= 76 and rdgpercent <= 78:
                print("Grade/Mark: 2.75")
                print("Description: Satisfactory")
            elif rdgpercent == 75:
                print("Grade/Mark: 3.0")
                print("Description: Passing")
            elif rdgpercent >= 65 and rdgpercent <= 74:
                print("Grade/Mark: 5.0")
                print("Description: Failure")

#Example:
#Input grade: 87.6
#Grade/Mark: 1.75
#Description: Very Good