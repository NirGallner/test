"""
String manipulation
"""

a = 'one quote'
b = "two qoutes"
c = """three quotes"""

# Show variables in strings
print("one string: {0}, second string: {1}, third string: {2}".format(a, b, c))
print(f"This is the last string: {c}")

# Built in functions for strings
print("Capital will do: " + "capital".capitalize())
print("Replace will do: " + "NUR".replace("U", "I"))
print("Alpha Numeric checker: " + str("AlphaNumeric".isalpha()))
print("Alpha Numeric checker, socond try: " + str("NotAlphaNumeric3".isalpha()))
print("123".isdigit())

# Split
print("Some, CSV, Value".split(","))
split = "This is a Split".split(" ")
print("The 4th word in the split variable is: " + split[3])

# Boolean and None
nonType = None
print("This is a none type: " + str(nonType))

trueValue = True
falseValue = False
print("This is true: {0}, and this is false: {1}".format(trueValue, falseValue))

# If statements
number = 5
if number == 5:
    print("Yes, it is")
else:
    print("No, it is not!!")
