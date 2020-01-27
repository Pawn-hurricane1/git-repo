fileptr1=open("first","r+");
fileptr2=open("second","w");
for i in fileptr1:
    #print(i);
    if "s" in i:
        print(i);
        #i=i.replace("s","");
        #fileptr1.write(i);
        fileptr2.write(i);
fileptr1.close();
fileptr2.close();
print("completed");
