import os,re,json
def check_file(filename):
    if not os.path.exists(filename):
        a=open(filename,"w+")
        a.write("[]")
def read_data(filename):
    b=open(filename,"r")
    c=json.loads(b.read())
    return c
def signup(filename):
    user=input("enter the name")
    password=(input("enter the password"))
    if not(re.search("[a-z A-Z]",password,)  and re.search('[0-9]',password) and re.search('[@#$]',password)):
        print("invalid password")
        return " "
    com_password=input("comfirm your password")
    if password!=com_password:
        print("password did not match")
        return " "
    contact=input("enter the contact")
    if len(contact)==10:
        email=input("enter the email")
        json_data=read_data(filename)
        for u in json_data:
            if u ["name"]==user:
                print("user already exists")
                return" "
        json_data.append({"name":user,"password":password,"contact":contact,"email":email})
        a=open(filename,"w+")
        b=json.dumps(json_data,indent=2)
        a.write(b)
        print("signup successfully")
    else:
        print("check the contact number")
def login(filename):
    user1=input("enter the username")
    password=input("enter the password")
    json_data=read_data(filename)
    for user in json_data:
        if user["name"]==user1:
            break
    else:
        print("this user isnt exist")
        return " " 
    if user["password"]!=password:
        print("plese check your password")
        return" "
    print("login successfully") 
filename="signup.json"
check_file(filename)
print("    WELCOME TO LOGIN SIGNUP      ")
choice=input("enter the choice:- if you want to  signup[1] ,if you want login in [2] ")
if choice=="1":
    signup(filename) 
elif choice=="2":
    login(filename)
else:
    print("check your choice")    
