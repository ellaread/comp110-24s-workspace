"""The file where I import stuff."""

from lessons import my_functions

# __name__ == "__main__":
print(my_functions.add(4,5))

# from package name (or directory or file) import module name

#function module name.functionname(arguments)
#variable modulename.variablename

# another way to import functions 
    # from packagename.modulename import functionname

from lessons.my_functions import double, double_display

print(double(1))
double_display(4)