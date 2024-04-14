def xor(a,b):
    if a==0 and b==0:
        return 0
    elif a==1 and b==1:
        return 0
    else:
        return 1

def printpoly(num,poly):
    print('a'+str(num),'=',end=' ')
    for i in range(7,-1,-1):
        if poly[i]==1:
            print('x^'+str(i),end=' ')
        else:
            print('   ',end=' ') 
    print('')


primpoly = [1,0,0,0,1,1,1,0,1]
testpoly = [1,0,0,0,0,0,0,0]

printpoly(1,testpoly)

for i in range(255):
    temp=[0]
    for j in range(8):
        temp.append(testpoly[j])
    testpoly = temp
    
    if testpoly[8]==1:
        for j in range(9):
            testpoly[j]=xor(testpoly[j],primpoly[j])
    printpoly(i+1,testpoly)

    