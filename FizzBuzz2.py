import sys

#n = 100

if sys.argv[1:]:
    my_input = sys.argv[1:]
else:
    my_input = input("please enter a value: ")

    user_input = int(my_input)

for i in range(1, user_input):

    if i % 15 == 0:
        print("fizzbuzz")

    elif i % 3 == 0:
            print("fizz")

    elif i % 5 == 0:
        print("buzz")

    else:
        print(i)



