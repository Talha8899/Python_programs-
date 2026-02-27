#this programe takes a list and return its aerage  

#fuction for calculate average
def list_averg(list):
   averg=sum(list)/len(list)
   print (averg)
   return averg

#this part takes list elements from user as input
mylist=[]
while True:
    mylist_items=input("enter the list values and write break when you done:")
    if (mylist_items.lower()=="break"):
        break
    mylist.append(int(mylist_items))
    print(mylist)

# call for calculate averg
list_averg(mylist)