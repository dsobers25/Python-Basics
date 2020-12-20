# 1. Comments
#-----------------------------------------------------------------
# This is a single-line comment

""" This is a multi-line
comment. If you ever need
to use more than one line for
a comment, use triple double
quotes. """

# 2. Variable assignments
# Python does not require programmers to explicitly use data types
#----------------------------------------------------------------- 
# this is an integer assignment
x1 = 10
# this is a String assignment
x2 = "11"
print("Value of x2= \"%s\"" % x2)
print("Value of x1= %d" % x1)

typeOfx1 = type(x1)
typeOfx2 = type(x2)

# 3. Casting
# cast variables to integers, floats or strings using
# int() and str() and float()
print("===================== Casting Integer -> String ========================")
print("The data type of variable \"x1\" is %s" % type(x1))
print("The value of \"x1\" is -> %d" % x1)
print("Casing x1 to a String Data Type")
x1 = str(x1)
print("The value of \"x1\" is -> \"%s\"" % x1)
print("The data type of variable \"x1\" is now %s" % type(x1))

print("===================== Casting String -> Integer ========================")
print("The data type of variable \"x2\" is %s" % type(x2))
print("The value of \"x2\" is -> \"%s\"" % x2)
print("Casing x2 to a Integer Data Type")
x2 = int(x2)
print("The value of \"x2\" is -> %s" % x2)
print("The data type of variable \"x2\" is now %s" % type(x2))

print("===================== Casting Integer -> Float ========================")
print("The data type of variable \"x2\" is %s" % type(x2))
print("The value of \"x2\" is -> %d" % x2)
print("Casing x2 to a Float Data Type")
x2 = float(x2)
print("The value of \"x2\" is -> %.2f" % x2)
print("The data type of variable \"x2\" is now %s" % type(x2))