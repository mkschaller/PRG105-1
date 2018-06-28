"""
Complete all of the TODO directions
Your file should compile error free
Submit your completed file
"""

# TODO 2.3 display output with the string function -
#   write two lines of code:
#   the first one displays your name
#   the second displays your major
print('McKenna Schaller')
print('\nGraduated with an AAS in Web Design and Development and an AAS in Graphic Arts from MCC.')

# TODO 2.3 using quotes
#   Write a statement that displays
#   The dog says "woof!"
print('The dog says "woof!"\n')
s
# TODO 2.4 working with and printing variables
#   Declare a variable named age, and set the initial value to your age
#   Print the variable
#   Print the word age with a space and the variable
#   Assign the variable 42 to the age variable
#   Print the variable
#   Print the word age with a space and the variable
age = 22
print(age)
print('Age:', age)
age = 42
print(age)
print('Age:', age, '\n')

# TODO 2.6 keyboard input
#   Get the user to enter their name and assign it to the variable name
#   Print a line that greets the user by name (Hello, Meri)
name = input('Enter your name: ')
print('Greetings, ' + name + '!\n')

# TODO 2.6 - 2.7 numeric input, performing calculations
#   Get the user to enter their age, store it as an integer
#   Print "This year you are ", age <-- please note, a comma creates a list of values
#   when using a comma in a print statement, you can mix numbers and strings
#   Add 1 to the age (age = age + 1)
#   Print "Next year you will be ", age
age = int(input('How old are you? '))
print('This year you are ' + str(age) + '.')
age += 1
print('Next year, you will be ' + str(age) + '.\n')

# TODO 2.7 performing calculations
#   Calculate 7 divided by 2, print the equation and the result
#   Calculate the remainder of 7 divided by 2, use the modulus operator, print the equation and the result
answer = 7 / 2
print('7 divided by 2 is', answer, '\n')

# TODO 2.7 data conversion
#   Write an equation that divides an integer by an integer, display the equation and the result with a print statement
#   Write an equation that divides an float by a float, display the equation and the result with a print statement
#   Write an equation that divides an float by an integer, display the equation and the result with a print statement
divide_int = 2 / 2
print('2 divided by 2 is ', divide_int, '\n')
divide_float = 4.5 / 1.2
print('4.5 divided by 1.2 is ', divide_float, '\n')
divide_float_int = 6.7 / 4
print('6.7 divided by 4 is ', divide_float_int, '\n')

# TODO 2.8 Output
#   modify the following code to print on one line, without merging the lines of code. Separate the words with a hyphen
print('one', end=' ')
print('two', end=' ')
print('three', end='.\n')

# TODO 2.8 Output
#   Modify the following line of code to add tabs between the days of the week
print("Sunday \tMonday \tTuesday \tWednesday \tThursday \tFriday \tSaturday")


# TODO 2.8 Concatenating strings
#   Have the user enter their name
#   Greet the user, concatenate hello and their name into one string
name = input('Enter your name: ')
greeting = 'Hello, ' + name
print(greeting)


# TODO 2.8 Formatting Numbers
#   Change the output so that it is formatted to display a minimum field width of 30
#   include commas, with only
#   two numbers showing to the right of the decimal point
#   example:
#                 6,548,974,897.57
number = 6548974897.5687979797
print(format(number, '30.2f'))


# TODO 2.8 Formatting percentage
#   Format the following as a percentage with 2 as the precision
percentage = .7654
print(format(percentage, '.2%'))
