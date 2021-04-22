from one_player_tic_tac_toe_func import *
k=1
while(k):
    fl=0
    count =0
    j=0
    print('PLAYER 1 HAS X AND COMPUTER HAS O')
    print('AND THE GAME BEGINS!!!!')
    a=['1','2','3']
    b=['4','5','6']
    c=['7','8','9']
    print('\n',a,'\n',b,'\n',c)
    player(a,b,c)
    count+=1
    print('\n',a,'\n',b,'\n',c)
    comp1(a,b,c)
    count+=1
    print('\n',a,'\n',b,'\n',c)
    player(a,b,c)
    count+=1
    print('\n',a,'\n',b,'\n',c)
    check_col_pl(a,b,c,j)
    check_row_pl(a,b,c,j)
    check_diag_pl(a,b,c,j)
    print(j)
    if j==1:
        comp1(a,b,c)
    count+=1
    print('\n',a,'\n',b,'\n',c)
    while 1:
        player(a,b,c)
        print('\n',a,'\n',b,'\n',c)
        count+=1
        if (check_col_cmp(a,b,c)==0 or check_row_cmp(a,b,c)==0 or check_diag_cmp(a,b,c)==0):
            fl=1
            break
        check_col_pl(a,b,c,j)
        check_row_pl(a,b,c,j)
        check_diag_pl(a,b,c,j)
        if j==1:
            comp1(a,b,c)
        if (check_col(a,b,c)==0 or check_row(a,b,c)==0 or check_diag(a,b,c)==0):
            fl=1
            break
        if(count==9):
            break
        print('\n',a,'\n',b,'\n',c)
        if (check_col(a,b,c)==0 or check_row(a,b,c)==0 or check_diag(a,b,c)==0):
            fl=1
            break
    if(fl==0):
        print('\nThe game ends in Tie')
    print('-----------------------------------------------------------')
    k=input('\nPress 1 if you want to play again press 1 else press 0: ')
print('THE GAME IS OVER ')
