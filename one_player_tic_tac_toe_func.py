def check_col(a):
    if a[0]==a[3]==a[6]:
        print ('CONGRATUALTIONS!',a[0],' WINNER!')
        return 1
    if a[1]==a[4]==a[7]:
        print ('CONGRATUALTIONS!',a[1],' WINNER!')
        return 1
    if a[2]==a[5]==a[8]:
        print ('CONGRATUALTIONS!',a[2],' WINNER!')
        return 1
def check_row(a):
    if a[0]==a[1]==a[2]:
        print ('CONGRATUALTIONS!',a[0],' WINNER!')
        return 1
    if a[3]==a[4]==a[5]:
         print ('CONGRATUALTIONS!',a[3],' WINNER!')
         return 1
    if a[6]==a[7]==a[8]:
        print ('CONGRATUALTIONS!',a[6],' WINNER!')
        return 1
def check_dia(a):
    for i in range(1):
        if a[0]==a[4]==a[8] or a[2]==a[4]==a[6]:
            print ('CONGRATUALTIONS!',a[4],' WINNER!')
            return 1            
def tic_tac_toe():
    print ("\nENJOY THE GAME!!\n")
    a=['1','2','3','4','5','6','7','8','9']
    print (a[0],' ',a[1],' ',a[2])
    print (a[3],' ',a[4],' ',a[5])
    print (a[6],' ',a[7],' ',a[8])
    flag=0
    while 1:
        print ("WHAT PLAYER1 WANTS TO TAKE 'X' or 'O'?")
        ch=input()
        if ch=='X' or ch=='O':
            if ch=='X':
                flagg=0
                ch1='O'
            else:
                flagg=1
                ch1='X'
            break
        else:
            print ("ONLY TWO OPTIONS AVAILABLE TO CHOOSE!")
    for i in range(5):
        while 1:
            x=input("ENTER LOCATION YOU WANT TO PLAY : ")
            if x>9 or x<1:
                print ("LOCATION NOT AVAILABLE!")
                continue
            elif a[x-1]=='X' or a[x-1]=='O':
                print ("LOCATION ALREADY OCCUPIED!")
            else:
                a[x-1]=ch
                break
        print (a[0],' ',a[1],' ',a[2])
        print (a[3],' ',a[4],' ',a[5])
        print (a[6],' ',a[7],' ',a[8])
        if check_col(a) or check_row(a) or check_dia(a):
            flag=1
            break
        if i==4:
            break
        for j in range(9):
            if a[j]=='X' or a[j]=='O':
                continue
            else:
                x1=j+1
                break;
        print ("\nCOMPUTER PLAYED ON",x1)
        a[x1-1]=ch1
        print (a[0],' ',a[1],' ',a[2])
        print (a[3],' ',a[4],' ',a[5])
        print (a[6],' ',a[7],' ',a[8])
        if check_col(a) or check_row(a) or check_dia(a):
            flag=1
            break
    if flag==0:
        print ("MATCH DRAW!")
    print ("PRESS 'Y' TO PLAY AGAIN ")
    ch=input()
    if ch=='Y':
        tic_tac_toe()
    else:
        print ("THANKS FOR PLAYING THE GAME!")
