# in this we use two approches for reading 
#replacing and wring in file
# approch 1
#open file to read data
with open("sample.txt") as f:
    data=f.read()
#open file to replace data
with open("sample.txt","w") as f:
    new_data=data.replace("java","python")
#open file to write new data and print it 
with open("sample.txt","+r") as f:
    f.write(new_data)
    f.seek(0)
    update=f.read()
    print(update)
#approch 2
#oprn file and read 
f=open("sample.txt","+r")
data=f.read()
#replace and write new data
new_data=data.replace("java","python")
f.seek(0)
f.write(new_data)
f.seek(0)
updated=f.read()
#print new data and close file
print(updated)
f.close()