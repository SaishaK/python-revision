#Homework question for python - revision: Arjun is the monitor of his class and his teacher told him to collect the email id of all the students.
#He created the list of email ids in a text file and now before he sends the list to his teacher, he wants to check whether all the email id in the list is valid or not.
#It will take a lot of time to verify it manually. To help him, create a program in python where he can enter the email id and the program will print valid if the email id is valid and not valid if the email id is not valid.
#Hint: Using membership operator check whether email id contains @ and .com. Also, make sure .com occurs at the end. Sample run example:>> hello@gmail.com → valid>> example@outlook.com → valid>> .com@first → invalid>> paypal → invalid

email = input("Enter the email id")

if "@" in email and email.endswith(".com"):
    print("The email is valid")
else:
    print("The email is invalid")
