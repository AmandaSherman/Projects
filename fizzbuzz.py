#Write a program that prints the numbers from 1 to 100.
#Multiples of three print “Fizz” instead of the number.
#Multiples of five print "Buzz".
#For multiples of both 3 and 5 print "FizzBuzz".

class FizzBuzz():

    for i in range(1,101):
        if (i % 5 == 0 and i % 3 == 0):
            print ("FizzBuzz")
        elif (i % 3 == 0):
            print ("Fizz")
        elif (i % 5 == 0):
            print ("Buzz")
        
        else:
            print (i)
