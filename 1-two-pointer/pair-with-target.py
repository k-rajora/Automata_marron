array=[3,2,4,4,5,4,3,3,5,1]
target=6
array.sort()
# counter=0
def answer(arr, target):
        result=[]
        l,r=0,len(arr)-1
        while l<r:
                checksum=arr[l]+arr[r]
                if checksum<target:
                        l+=1
                elif checksum>target:
                        r-=1
                else:
                    # counter+=1
                    result.append([arr[l],arr[r]])
                    l+=1
                    r-=1
        return result

print(len(answer(array,target)))

                

  
