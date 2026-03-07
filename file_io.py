#open file and write data in it 
#if file dosent exist it creat the file
with open("myfile.txt","+w")as f:
    f.write("hi i am talha \n")
    f.write("i am learning file i/o operation using python")
# add more data 
with open("myfile.txt","+a")as f:
    f.write("\nnice to meet you")
#read data from file and print it 
with open("myfile.txt")as f:
    data=f.read()
    print(data)