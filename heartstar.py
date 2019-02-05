for rows in range(6):
    for cols in range(7):
        if(rows==0 and cols%3!=0)or(rows==1 and cols%3==0)or(rows-cols==2)or(rows+cols==8):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()   
            
