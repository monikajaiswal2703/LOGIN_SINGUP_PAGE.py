import json
import re
import os.path

print("*** WELCOME TO LOGIN SINGUP PAGE ***")
login_singup=input("what is choose login or singup:-")
file=os.path.exists("text2.json")
if login_singup=="s":
    first_name=input("enter your first name:-")
    last_name=input("enter your last name:-")
    RegEx="[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|org)"
    email=input("enter your email:-")
    if (re.search(RegEx,email)):
        strong="[a-zA-Z0-9]+@[a-zA-Z0-9]"
        pass1=input("enter the password:-")
        if (re.search(strong,pass1)):
            con_pass=input("confirm your password:-")
            if pass1==con_pass:
                print("*** SINGUP SUCCESSFUL ***")
                dict={"first name":first_name,"last name":last_name, "email":email,"password":pass1}
                if file==True:
                    with open("text2.json","r") as f:
                        p=json.load(f)
                        p.append(dict)
                        p=json.dump(p,f,indent=4)
                        # with open("text2.json","w")as f:
                        #     f.write(p)
                        #     p=json.dumps(p)
                else:
                    with open("text2.json","a")as f:
                        json.dump([dict],f,indent=4)
                        
            else:
                print("password did not match")
        else:
            print("invvalid password")
    else:
        print("invalid email address")
else:
    if login_singup=="l":
        user2=input("enter the name:-")
        pass2=input("enter the password:-")
        with open("text2.json","r")as file2:
            b=json.load(file2)
            for i in b:
                if i["first name"]==user2:
                    print("your name is correct")
                    if i["password"]==pass2:
                        print("LOGIN SUCCESSFUL")
                    else:
                        print("LOGIN NOT SUCCESSFUL")
                else:
                    print("your user name is incorrect")
    else:
        print("YOU MADE A MISTAKE IN CHOOSING")

            

