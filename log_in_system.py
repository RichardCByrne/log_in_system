'''
1. Create an account DONE
    a. email
    b. username
    c. password
    d. re-type password
    e. create unique id for each account
    f. add account details to dictionary

2. Log in DONE
    a. Ask for username and password
    b. If correct, say "You have logged in successfully."
    c. If incorrect, give 3 tries before locking out for 60 seconds
    d. Create a user id allocated with their details

3. Log out
    a. Type "Log out" to log out of system

4. Count Log ins
    a. Count the number of times a user has logged in
    b. Print a list of users with their respective log in counts

5. Change password

6. Check to see if username has already been taken

7.Check to see if email address has already been used

8. Choose action home screen: either login or create an account
'''



import json


#List of all the users and their details
all_users = {}
number_of_users = len(all_users)

print("Welcome!\nTo create an account, please enter your email, a username and password below.")

#CREATING AN ACCOUNT
def create_account():
    #CREATING A PASSWORD
    #Creating blank password variables to compare against each other for password re-type verification
    first_password = ""
    re_password = ""
    confirmed_password = ""

    #Creating a function that allows the user to create a password
    def password_creator():
        global first_password
        global re_password
        global confirmed_password
        first_password = input("Enter a password: ")
        re_password = input("Please re-type your password: ")

        if first_password != re_password:
            print("\nYour passwords do not match. Please try again:")
            password_creator()

        else:
            return first_password

    #Getting input from the user
    email = input(str("Enter email address: "))
    username = input(str("Enter a username: "))
    confirmed_password = password_creator()
    log_in_count = 0
    is_logged_in = False

    # Adding to list of users
    global number_of_users
    all_users["User " + str(int(number_of_users) + 1)] = {"Email": email, "Username": username, "Password": confirmed_password, "Log in count": log_in_count, "Is logged in": is_logged_in}
    with open('All Users.txt', 'w') as file:
        file.write(json.dumps(all_users))

    print("\n")
    print("Your new account is up and running! Please log in below.")

    number_of_users = len(all_users)

    login()

'''    #Printing the number of users
    if number_of_users == 0:
        print("There are " + str(number_of_users) + " users.")
    elif number_of_users == 1:
        print("There is " + str(number_of_users) + " user.")
    elif number_of_users > 1:
        print("There are " + str(number_of_users) + " users.")'''











#LOGGING IN
def login():
   login_email = str(input("\nTo log in, please first enter your email address: "))
   login_password = str(input("Now please enter your password: "))
   global is_logged_in

   for u_id, u_info in all_users.items():
       print("\nUser ID: " + u_id)

       if u_info["Password"] == login_password and u_info["Email"] == login_email:
           u_info["Log in count"] += 1
           u_info["Is logged in"] = True
           with open('All Users.txt', 'w') as file:
               file.write(json.dumps(all_users))
           print("Hi " + u_info["Username"] + "! Welcome to your new account. You can do approximately 0 things with your new account.\nThanks for stopping by!")
       elif u_info["Password"] != login_password:
           print("Incorrect password. Please try again.")
           login()

       elif u_info["Email"] != login_email:
           a_or_b = input("Email address has not been used to create an account. Would you like to create an account, or try again?\nPress 'a' to create account now, or 'b' to try again.")
           if a_or_b == "a" or "A":
               create_account()
           elif a_or_b == "b" or "B":
               login()
           else:
               print("Looks like you didn't input a proper answer. You've broken the system now. Hi five. :)")











create_account()