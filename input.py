import time


number = int(input("Enter a number: "))
print("Your number is %d" % (number))


while True:

    i = 1
    x = number
    while i <= number:
        while x >= i:
            print("*"*x)
            x -= 1
        i+= 1

    time.sleep(0.5)

    i = number
    x = 2
    while i >= number:
        while x <= i:
            print("*"*x)
            x += 1
        i -= 1
    time.sleep(0.05)




