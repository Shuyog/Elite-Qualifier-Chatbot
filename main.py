import time
print("To aCceSs ThIs ChatbOt, eNter tHe PaSSword. hint: capitalization")

guess = input("Password: ")
password = '1'

while guess != password:
  print('Incorrect password.')
  guess = input('Password: ')



print("Hi there what is your name? ")
name = input()

print("How are you " + name + "?")
response = input()

if response == "Good":
  print("That's good to hear")
elif response == "Not well": 
  print("Well that's unfortunate")
else:
  print("Please respond with either Good or Not well ") 

choices = "Good"
#I wasn't sure how to add 2 choices. I tried using or but it didn't work so i left it like this
while response != choices:
  print("Invalid, please try again")
  response = input()


print("Quick! Answer this riddle! You're running a race and pass the person in 2nd place. What place are you in now? ")

response2 = input()
rAnswer = "2nd place"
if response2 == "2nd place":
  print("Good job! You got it correct!")
else:
  print("Wrong, try again")

while response2 != rAnswer:
  print("Did you type it like this? i.e.: 5th place.")
  response2= input()

print("SYSTEM HAS BEEN HACKED")

print("Error Error, bot will be deleted in 5 seconds")

def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("ZZZzzz")
countdown(5)

