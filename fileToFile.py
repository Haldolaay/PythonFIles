file1=open("data.txt","r")
file2=open("result.txt","w")
counter = 0
obj =[]
# Iterate over each line in the file
for line in file1.readlines():

    # Separate each item in the line
    items=line.split()
    print(items)
    # Retrieve important bits
    qty=items
    reorder=items
    # obj[counter] = {'label':items[0], 'value':items[1]}
    # counter+=1
    # Write to the file if conditions are met
    if qty<=reorder:
        file2.write('{label:"'+items[0]+"\"\t"+'value: "'+items[1]+"\"},\n")
    
# Release used resources
print(obj)
file1.close()
file2.close()
