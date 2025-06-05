class Chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook. How would you like to proceed?
                           1. Press 1 to sign-up.
                           2. Press 2 to sign-in.
                           3. Press 3 to write a post.
                           4. Press 4 to message a friend.
                           5. Press any other key to exit""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input =="3":
            self.my_post()
        elif user_input == "4":
            self.send_message()
        else:
            exit()

    def signup(self):
        email = input("Enter your email : ")
        password = input("Enter your password : ")
        self.username = email
        self.password = password
        print("Signed-up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password=='':
            print("Please sign-up first by pressing 1 in the menu.")
        else:
            uname = input("Enter your email/username here : ")
            password = input("Enter your password : ")
            if self.username == uname and self.password == password:
                print("You have signed-in successfully.")
                self.loggedin = True
            else:
                print("Please enter the correct credentials.")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("Write a post...")
            print(f"Your post has been done. Take a look here - {txt}")
        else:
            print("You need to sign-in first to post something.")
        print("\n")
        self.menu()

    def send_message(self):
        if self.loggedin==True:
            txt = input("Enter your message : ")
            friend = input("Whom to send the message? : ")
            print(f"Your message has been sent to {friend}.")
        else:
            print("You need to sign-in first to post something.")
        print("\n")
        self.menu()

# obj = Chatbook()