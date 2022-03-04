def Search(self,num,target):
    for i in range(len(num)):
        if num[i]<target and num[i+1]>target:
            return i+1
        else:
            return i
    return None
num=[1,2,4,5]
target=[3]
print(Search(num, target))
