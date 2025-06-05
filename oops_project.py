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
            pass
        elif user_input == "4":
            pass
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

obj = Chatbook()