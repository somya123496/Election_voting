'''import xlwt
wb=xlwt.Workbook()
ws=wb.add_sheet('election')
ws.write(0,0,'s.No')
ws.write(0,1,'candidate_Name')
ws.write(0,2,'votes')
for i in range(1,6):
    ws.write(i,0,i)
    name=input('enter name of candidate%d'%i)
    ws.write(i,1,name)
    vt=int(input('enter no of votes'))
    ws.write(i,2,vt)
wb.save('election info.xls')
input()'''


from xlrd import open_workbook
from xlutils.copy import copy
b=open_workbook('election info.xls')
fs=b.sheet_by_index(0)
wb=copy(b)
ws=wb.get_sheet(0)
votes=fs.col_values(2)
votes.pop(0)
print(votes)
kd=fs.col_values(0)
kd.pop(0)
print(kd)

while(True):
    m=int(input('enter number'))
    if m==1:
        votes[0]+=1
        print(votes)
    elif m==2:
        votes[1]+=1
        print(votes)
    elif m==3:
        votes[2]+=1
        print(votes)
    elif m==4:
        votes[3]+=1
        print(votes)
    elif m==5:
        votes[4]+=1
        print(votes)
    elif m==6:
        s='somya'
        r=len(votes)
        result=max(votes)
        p=4
        print('enter password')
        for i in range(0,3):
            p=p-1
            print('u have',+ p,'attempts left')
            x=input()
            if x==s:
                for i in range(0,r):
                    if (votes[i]==result):
                        print('winner is candidate' + '  ' +str(i+1))
                break
            else:
                 print('wrong password......try again')
                        
    elif m==7:
        '''j=4
        print(' to exit enter password to confirm')
        for i in range(0,3):
            j=j-1
            print('u have',j,'attempts left')
            x=input()
            if(x==s):
                print('exit')
                break
            else:'''
        print('exit')
        break
'''for j in range(0,5):'''
#ws.write(i+1,2,votes[i])
wb.save('election info.xls')    
                
                
                    
