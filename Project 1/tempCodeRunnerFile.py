'''
 1 = snake
-1 = water
 0 = gun'''
computer=-1
youstr=input("Enter Your Choice: ")
youdict={"snake":1, "water":-1, "gun":0}
reversedict={1:"snake", -1:"water", 0:"gun"}
younum=youdict[youstr]
if(computer==1 and younum==0):
    print("YOU WIN !")
elif(computer==1 and younum==-1):
    print("YOU LOSE TRY AGAIN !")
elif(computer==-1 and younum==0):
    print("YOU LOSE TRY AGAIN !")
elif(computer==0 and younum==1):
    print("YOU LOSE TRY AGAIN !")

elif(computer==younum):
    print("DRAW TRY AGAIN !")
else:
    print("SOMETHING WENT WRONG !")


