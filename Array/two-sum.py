# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

nums = [5 , 6 , 2 , 3 , 11, 15]
target = 9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):            
        if(nums[i]+nums[j]==target):
            print("indices",i,j)

