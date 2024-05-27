d = {}
while True:
    menu = """

        press 1 for signup
        press 2 for login
        press 3 for Otp
        press 4 for exit
    """
    print("menu")
    
    Choice = int(input("Enter choice : "))
    
    if Choice==1:
        email = input("Enter Email : ")
        name = input("Enter Name : ")
        mobile = int(input("Enter Mobile number : "))
        password = input("Enter password : ")
        cpassword = input("Enter confirm password!!")
        

        if password==password:
            d[name]=name
            d[email]=email
            d[password]=password
            d[mobile]=mobile
            print("signup sucessfully!!")
        else:
            print("password and confirm password does not match!!")
    elif Choice==2:
        name = input("Enter Name : ")
        password = input("Enter password : ")
        print("Login succesfuly!!")
    else Choice==3:
        Otp = []
        Otp = input("Enter opt : ")
        print("Thank You!!")
       