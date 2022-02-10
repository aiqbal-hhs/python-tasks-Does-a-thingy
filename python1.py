name = input("Who are you?")
name = name.strip().lower()
if name == "oliver":
    print("Mine too!")
birth_date = int(input("When where you born?"))
age = 2022 - birth_date
print("you will be {} years old this year!".format(age))

length = int(input('what is the length of your rectangle?'))
width = int(input('what is the width of your rectangle?'))
area = width * length
print('the area of the rectangle is {}!'.format(area))

print('I am wasting my own time! ' * 8)

string1 = "tis' but a scratch! "
string2 = "but your arm is missing!"
print(string1 + string2)
