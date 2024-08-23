#თქვენი დავალება იქნება გააკეთოთ ბანკის სისტემა მოცემული სექციებით პითონში,რაც აქამდე ისწავლეთ გააკეთეთ იმ მასალით გამოიყენეთ თქვენი მაქსიმალური ცოდნა,მერე კი ჩვენ შევამოწმეთ თუ რა დონის ცოდნა გამოიყენეთ და იმის მიხედვით შეიგიმოწმებთ


print("saqartvelos banki")


registered_password = "ani123"

authorizad = False
while authorizad != True:
    user_input = input("enter the user: ")

    if user_input == registered_password:
        print("main page ")
        authorizad = True
    else:
        print("the user is invalid")


num = int(input("enter number: "))
address = input("enter address")


age = int(input('enter your age: '))
num1 = 20

while age == num1:
    print("you are an adult")
    break
else:
    print("you are underage")



print("samushao dgeebi")



num = int(input("enter you number: "))
if num == 1:
    print("otxshabati")
elif num == 2:
    print("paraskevi")



