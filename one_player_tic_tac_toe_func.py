import random
def check_col(a,b,c):
    for i in range(3):
        if a[i]==b[i]==c[i]=='X':
            print( '\nPlayer wins!!!')
            return 0

def check_row(a,b,c):
    for i in range(1):
        if a[i]==a[i+1]==a[i+2]=='X':
            print( '\nPlayer wins!!!')
            return 0
        elif b[i]==b[i+1]==b[i+2]=='X':
            print( '\nPlayer wins!!!')
            return 0
        elif c[i]==c[i+1]==c[i+2]=='X':
            print( '\nPlayer wins!!!')
            return 0
        

def check_diag(a,b,c):
    for i in range(1):
        if a[i]==b[i+1]==c[i+2]=='X':
            print( '\nPlayer wins!!!')
            return 0
        elif c[i]==b[i+1]==a[i+2]=='X':
            print( '\nPlayer wins!!!')
            return 0
        

def comp1(a,b,c):
    if b[1]!='X':
        b[1]='O'
    else:
        k=random.choice([1,3,7,9])
        l=random.choice([2,4,6,8])
        if k==1 or k==3 and a[k-1]!='X' and a[k-1]!='O':
            a[k-1]='O'
        elif k==7 or k==9 and c[k-7]!='X' and a[k-7]!='O':
            c[k-7]='O'
        elif l==2 and a[1]!='O' and a[1]!='X':
            a[1]='O'
        elif l==8 and c[1]!='O' and c[1]!='X':
            c[1]='O'
        elif l==4 or l==6 and b[l-4]!='X' and b[l-4]!='O':
            c[k-7]='O'

    

def player(a,b,c):
    x=input('PLAYER : ')
    x=int(x)
    if(x<=3):
        if a[x-1]=='O'or a[x-1]=='X':
            print( 'sorry,choose someother digit.')
            player1(a,b,c)    
        else:
            a[x-1]='X'
    elif(x<=6):
        if b[x-4]=='O'or b[x-4]=='X':
            print( 'sorry,choose someother digit.')
            player1(a,b,c) 
        else:
            b[x-4]='X'
    elif(x<=9):
        if c[x-7]=='O'or c[x-7]=='X':
            print( 'sorry,choose someother digit.')
            player1(a,b,c) 
        else:
            c[x-7]='X'


def check_col_cmp(a,b,c):
    for i in range(3):
        if a[i]==b[i]=='O'and c[i]!='X' and c[i]!='O':
            c[i]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif a[i]==c[i]=='O'and b[i]!='X' and b[i]!='O':
            b[i]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif b[i]==c[i]=='O'and a[i]!='X' and a[i]!='O':
            a[i]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
def check_row_cmp(a,b,c):
    for i in range(1):
        if a[i]==a[i+1]=='O' and a[i+2]!='X' and a[i+2]!='O':
            a[i+2]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif a[i]==a[i+2]=='O'and a[i+1]!='X' and a[i+1]!='O':
            a[i+1]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif a[i+1]==a[i+2]=='O' and a[i]!='X' and a[i]!='O':
            a[i]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif b[i]==b[i+1]=='O' and b[i+2]!='X' and b[i+2]!='O':
            b[i+2]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif b[i]==b[i+2]=='O'and b[i+1]!='X' and b[i+1]!='O':
            b[i+1]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif b[i+1]==b[i+2]=='O' and b[i]!='X' and b[i]!='O':
            b[i]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif c[i]==c[i+1]=='O' and c[i+2]!='X' and c[i+2]!='O':
            c[i+2]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif c[i]==c[i+2]=='O'and c[i+1]!='X' and c[i+1]!='O':
            c[i+1]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif c[i+1]==c[i+2]=='O' and c[i]!='X' and c[i]!='O':
            c[i]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        else:
            return 1
        

def check_diag_cmp(a,b,c):
    for i in range(1):
        if a[i]==b[i+1]=='O' and c[i+2]!='X' and c[i+2]!='O':
            c[i+2]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif a[i]==c[i+2]=='O' and b[i+1]!='X' and b[i+1]!='O':
            b[i+1]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif c[i+2]==b[i+1]=='O' and a[i]!='X' and a[i]!='O':
            a[i]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif c[i]==b[i+1]=='O' and a[i+2]!='X' and a[i+2]!='O':
            a[i+2]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif c[i]==a[i+2]=='O' and b[i+1]!='X' and b[i+1]!='O':
            b[i+1]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0
        elif a[i+2]==b[i+1]=='O' and c[i]!='X' and c[i]!='O':
            c[i]='O'
            print( a,'\n',b,'\n',c)
            print( 'Computer wins!!!')
            return 0        

def check_col_pl(a,b,c,j):
    for i in range(3):
        if a[i]==b[i]=='X'and c[i]!='X' and c[i]!='O':
            c[i]='O'
            j=1
        elif a[i]==c[i]=='X'and b[i]!='X' and b[i]!='O':
            b[i]='O'
            j=1
        elif b[i]==c[i]=='X'and a[i]!='X' and a[i]!='O':
            a[i]='O'
            j=1
def check_row_pl(a,b,c,j):
    for i in range(1):
        if a[i]==a[i+1]=='X' and a[i+2]!='X' and a[i+2]!='O':
            a[i+2]='O'
            j=1
        elif a[i]==a[i+2]=='X'and a[i+1]!='X' and a[i+1]!='O':
            a[i+1]='O'
            j=1
        elif a[i+1]==a[i+2]=='X' and a[i]!='X' and a[i]!='O':
            a[i]='O'
            j=1
        elif b[i]==b[i+1]=='X' and b[i+2]!='X' and b[i+2]!='O':
            b[i+2]='O'
            j=1
        elif b[i]==b[i+2]=='X'and b[i+1]!='X' and b[i+1]!='O':
            b[i+1]='O'
            j=1
        elif b[i+1]==b[i+2]=='X' and b[i]!='X' and b[i]!='O':
            b[i]='O'
            j=1
        elif c[i]==c[i+1]=='X' and c[i+2]!='X' and c[i+2]!='O':
            c[i+2]='O'
            j=1
        elif c[i]==c[i+2]=='X'and c[i+1]!='X' and c[i+1]!='O':
            c[i+1]='O'
            j=1
        elif c[i+1]==c[i+2]=='X' and c[i]!='X' and c[i]!='O':
            c[i]='O'
            j=1
        

def check_diag_pl(a,b,c,j):
    for i in range(1):
        if a[i]==b[i+1]=='X' and c[i+2]!='X' and c[i+2]!='O':
            c[i+2]='O'
            j=1
        elif a[i]==c[i+2]=='X' and b[i+1]!='X' and b[i+1]!='O':
            b[i+1]='O'
            j=1           
        elif c[i+2]==b[i+1]=='X' and a[i]!='X' and a[i]!='O':
            a[i]='O'
            j=1
        elif c[i]==b[i+1]=='X' and a[i+2]!='X' and a[i+2]!='O':
            a[i+2]='O'
            j=1

        elif c[i]==a[i+2]=='X' and b[i+1]!='X' and b[i+1]!='O':
            b[i+1]='O'
            j=1
        elif a[i+2]==b[i+1]=='X' and c[i]!='X' and c[i]!='O':
            c[i]='O'
            j=1
