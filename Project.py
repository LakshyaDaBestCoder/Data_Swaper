def swapFileData():
    data_a=""
    data_b=""
    file1=input("Enter the name of the file you want to swap")
    print(file1)
    file2=input("Enter the name of the file you want to swap with")
    print(file2)
    with open(file1,"r") as a:
        data_a = a.read()
    with open(file2,"r") as b:
        data_b = b.read()
    with open(file1,"w") as a:
        a.write(data_b)
    with open(file1,"w") as b:
        b.write(data_a)
    print("The Data in ", file1, "is:", open(file1, "r"))
    print("The Data in ", file2, "is:", open(file2, "r"))
swapFileData()