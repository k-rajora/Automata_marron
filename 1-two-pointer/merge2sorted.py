arr1=[1,3,5,5]
arr2=[2,4,6,7,8,9,10]

answer=[]

man,women=0,0
m,n=len(arr1),len(arr2)
while man<m and women<n:
    if arr1[man]<=arr2[women]:
        answer.append(arr1[man])
        man+=1
    else:
        answer.append(arr2[women])
        women+=1

answer.extend(arr1[man:])
answer.extend(arr2[women:])

print(answer)
print(-1+1)