# a=[1,2,3,1,5,6,2,9,3,0,0,5,3,6,8,7,9,1,1,9]
# b={}
# for i in a:
#     if i in b:
#         b[i]+=i
#     else:
#         b[i]=i
# print(b)

# dict={"add":{"a":3,"b":4,"c":5,"d":7}}
# key=input("entr key:-")
# value=int(input("enter the value"))
# for i,j in dict.items():
#     for k in j:
#         if k==key:
#             j[k]+=value
# print(dict)

d1=["first name","email","password"]
d2=["monika","mj@gmail","mj@1234"]
d={}
l=[]
for i in d1,d2:
    d.update({d1(i),d2(i)})
print(d)
# l.append(d)
# print(l)


# dict={"add":{"a":3,"b":4,},"mlty":{"c":5,"d":7}}
# a=[]
# c={}
# for i ,j in dict.items():
#     if dict[i]==j:
#         a.append(j)
#         c.update({i:a})

# print(c)

# dictA = {"id": "0001","name": "hotdog","image":{"url": "images/0001.jpg","thumbnail":
# {"url": "images/thumbnails/0001.jpg","height,width": "2x4"}}}
# d={"add":{"a":3,"b":4,},"mlty":{"c":5,"d":7}}
# def dict_flatten(in_dict, dict_out=None, parent_key=None, separator="_"):
#    if dict_out is None:
#       dict_out = {}

#    for k, v in in_dict.items():
#       k = f"{parent_key}{separator}{k}" if parent_key else k
#       if isinstance(v, dict):
#          dict_flatten(in_dict=v, dict_out=dict_out, parent_key=k)
#          continue

#       dict_out[k] = v

#    return dict_out

# final_dict = dict_flatten(d)
# print(final_dict)

# with open("q9shopping_file.json","r") as file:
#     data=json.load(file)

# import json
# login_singup=input("what is choose login or singup:-")
# if login_singup=="login":
#         user2=input("enter the name:-")
#         pass2=input("enter the password:-")
# with open("text.json","r")as f:
#     print(json.load(f))
    # print(b)
#             for i in b:
#                 if i["first name"]==user2:
#                     print("your name is correct")
#                     if i["password"]==pass2:
#                         print("LOGIN SUCCESSFUL")
#                     else:
#                         print("LOGIN NOT SUCCESSFUL")
#                 else:
#                     print("your user name is incorrect")
# else:
#    print("YOU MADE A MISTAKE IN CHOOSING")