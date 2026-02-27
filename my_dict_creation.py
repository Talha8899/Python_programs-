# This program takes key and values from user and creat a dictionary  

my_dict={}
while True:
    key=input("enter the key or enter break when done:")
    if (key.lower()=="break"):
        break
    value=input(f"enter the value for {key} :")
    my_dict[key]=value

print(my_dict)