# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, 
# with a space separating the digits.

name = list()
name.append("1")
name.append("6")
name.append("8")
name.append("9")
name.append("3")

name.reverse()

for name in name:
    print(name)