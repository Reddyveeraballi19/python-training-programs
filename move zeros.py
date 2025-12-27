
def moveZeros(nums):
    x=[]
    y=[]
    for i in range(len(nums)):
        if nums[i]==0:
            x.append(nums[i])
        else:
            y.append(nums[i])
    z=y+x
    print(z)
nums=[0,1,0,3,72]
moveZeros(nums)

#leetcode program
def moveZeros(nums):
    idx=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[idx]=nums[i]
            idx+=1
    for i in range(idx,len(nums)):
        nums[i]=0
    return nums
nums=[0,1,0,3,81]
print(moveZeros(nums))