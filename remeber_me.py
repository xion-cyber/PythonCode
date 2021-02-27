import json

#如果以前存储了用户名，就加载它
#否则，就提示用户输入用户名并存储它

file_name = 'username.json'
try:
    with open(file_name) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("What's your name?\n")
    with open(file_name,"w") as file_object:
        json.dump(username,file_object)
        print("We will remember you when you come back!")
else:
    print("Welcome back, " + username + " !")