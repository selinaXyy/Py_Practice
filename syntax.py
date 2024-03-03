#output: o
print("Hello"[-1])



#serves as commas for better readability
print(234_567_789)



#booleans are Capital Cases
correct = True
incorrect = False



#type casting
num = 12345
print("There are " + str(num) + " apples in the box.") #make sure data type compatibility



#exponent symbol
print(2 ** 3)



#only takes the int portion
print(int(2.5))
#rounds the int
print(round(2.67304, 2)) #specify decimal degits
#if a number is exactly half way between 2 integers, it rounds the number to the nearest even number



#floor
print(3 // 2) #equals int(3/2)



#f-string (automatically does data type conversion)
age = 20
height = 180
adult = False
print(f"Your age is {age}, your height is {height}\nAdult: {adult}")



#if, elif, else
age = int(input("How old are you? "))
if age < 18:
    print("Hehe you are a child.")
elif age < 21:
    print("Hehe adult but can't drink.")
else:
    print("Ok you can drink but you are old.")




#for loop
string = "APPLE".lower() #.lower() can be applied to a whole string
num_of_p = 0
for letter in string:
    if (letter == "p"):
        num_of_p += 1

#ALTERNATIVELY
#num_of_p = string.count("p")
print(num_of_p)




#''' --> allows you to create multiple lines of a string
print(''' .d8888b.  .d8888b. 8888888888 
d88P  Y88bd88P  Y88b      d88P 
888    888888    888     d88P  
888    888888    888    d88P   
888    888888    888 88888888  
888    888888    888  d88P     
Y88b  d88PY88b  d88P d88P      
 "Y8888P"  "Y8888P" d88P  ''')



#for loop within a range
for number in range (0, 21, 2): #start(inclusive), stop(exclusive), step
    print(number)



#