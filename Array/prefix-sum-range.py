arr = [3,5,2,7,4]

prefix = [0]*len(arr)
prefix[0]= arr[0]

for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
print(prefix)

# sum from index 1 to 3:

left = 1
right = 3

if left==0:
    result = prefix[right]
else:
    result = prefix[right]-prefix[left-1]

print("Sum of indexes from 1 to 3 is : ",result)        