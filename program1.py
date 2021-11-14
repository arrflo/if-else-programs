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
def conditions():
    _incomplete = input("If the student is incomplete, type 'Y' and 'N' if not.")
    _withdrawn = input("If the student is withdrawn, type 'Y' and 'N' if not.")
    _dropped = input("If the student is dropped out, type 'Y' and 'N' if not.")
    return _incomplete, _withdrawn, _dropped

#variables
incomplete, withdrawn, dropped = conditions ()
gPercent = getGradePercentage()


# aask kung ang student ba ay incomplete, withdrawn, dropout


#Example:
#Input grade: 87.6
#Grade/Mark: 1.75
#Description: Very Good