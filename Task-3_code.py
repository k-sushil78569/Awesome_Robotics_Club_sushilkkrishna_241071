path=[
    ['S', '.', '.', '.', '.', '~', '.', '.', '^', '.'],
    ['#', '#', '#', '.', '.', '~', '#', '.', '^', '.'],
    ['.', '.', '.', '#', '.', '.', '#', '.', '.', '.'],
    ['.', '~', '~', '#', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '#', '#', '#', '#', '.'],
    ['^', '^', '.', '.', '.', '.', '.', '.', '~', '.'],
    ['#', '.', '.', '.', '.', '#', '~', '~', '~', '.'],
    ['.', '.', '#', '#', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '^', '^', '^', '^', 'G'],
    ['.', '#', '#', '#', '#', '#', '#', '.', '.', '.']
]
def up(cd,g):
    np=[cd[0]-1,cd[1]]
    if cd[0]>=1 and path[cd[0]-1][cd[1]]!='#' and np not in g:
        return 1
    else:
        return 0
def down(cd,g):
    np=[cd[0]+1,cd[1]]
    if cd[0]<9 and path[cd[0]+1][cd[1]]!='#' and np not in g:
        return 1
    else:
        return 0
def left(cd,g):
    np=[cd[0],cd[1]-1]
    if cd[1]>=1 and path[cd[0]][cd[1]-1]!='#' and np not in g:
        return 1
    else:
        return 0
def right(cd,g):
    np=[cd[0],cd[1]+1]
    if cd[1]<9 and path[cd[0]][cd[1]+1]!='#' and np not in g:
        return 1
    else:
        return 0
def createorappend(k,s):
    if len(k)==s:
        return 1
    else:
        return 0
    
val={'.':1,'~':3,'^':5,'G':1,'S':0}
nm=1
md={}
m1=[[[0,0]],0,0]
md[nm]=m1
while True :
    for i in list(md):
        s=len(md[i][0])
        cd=md[i][0][s-1]
        if md[i][1]!=md[i][2]:
            md[i][1]=md[i][1]+1
        else:
            if up(cd,md[i][0]):
                j=val[path[cd[0]-1][cd[1]]]
                if createorappend(md[i][0],s):
                    md[i][0].append([cd[0]-1,cd[1]])
                    md[i][1]=1
                    md[i][2]=j
                else:
                    nm=nm+1
                    s=md[i][0][:]
                    s.pop()
                    s.append([cd[0]-1,cd[1]])
                    md[nm]=[s,1,j]
            if down(cd,md[i][0]):
                j=val[path[cd[0]+1][cd[1]]]
                if createorappend(md[i][0],s):
                    md[i][0].append([cd[0]+1,cd[1]])
                    md[i][1]=1
                    md[i][2]=j
                else:
                    nm=nm+1
                    s=md[i][0][:]
                    s.pop()
                    s.append([cd[0]+1,cd[1]])
                    md[nm]=[s,1,j]
            if left(cd,md[i][0]):
                j=val[path[cd[0]][cd[1]-1]]
                if createorappend(md[i][0],s):
                    md[i][0].append([cd[0],cd[1]-1])
                    md[i][1]=1
                    md[i][2]=j
                else:
                    nm=nm+1
                    s=md[i][0][:]
                    s.pop()
                    s.append([cd[0],cd[1]-1])
                    md[nm]=[s,1,j]
            if right(cd,md[i][0]):
                j=val[path[cd[0]][cd[1]+1]]
                if createorappend(md[i][0],s):
                    md[i][0].append([cd[0],cd[1]+1])
                    md[i][1]=1
                    md[i][2]=j
                else:
                    nm=nm+1
                    s=md[i][0][:]
                    s.pop()
                    s.append([cd[0],cd[1]+1])
                    md[nm]=[s,1,j]
    p=0
    for j in list(md):
        w=len(md[j][0])
        sum=-1
        if [8,9] in md[j][0]:
            p=p+1
            print("path",p)
            for n in range(w):
                print(md[j][0][n])
                sum=sum+val[path[md[j][0][n][0]][md[j][0][n][1]]]
            print("cost=",sum)
    if p>0:
        break
