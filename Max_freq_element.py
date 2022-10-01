y=True
while(y):
    String=input("enter a string: ")
    dict={}
    for i in String:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    result= max(dict,key=dict.get)
    print("Most frequent character: ",result)
    check=input("Do you want to enter another string:(Y/N)")
    print()
    if check=='y'or check=='Y':
        y=True
    else:
        y=False