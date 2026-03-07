with open("myfile.txt","+w")as f:
    f.write("hi i am talha \n")
    f.write("i am learning file i/o operation using python")
with open("myfile.txt","+a")as f:
    data=f.read()
    print(data)
    