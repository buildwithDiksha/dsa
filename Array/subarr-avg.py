arr = [2,2,2,2,5,5,5,8]
k=3
arr_sum = 0
threshold=4
count=0

for i in range(k):
    arr_sum=arr_sum+arr[i]
avg = arr_sum/k

if avg>=threshold:
    count=count+1

for i in range(k,len(arr)):
    arr_sum = arr_sum-arr[i-k]+arr[i]
    print(arr_sum)

    avg= arr_sum/k

    if avg>=threshold:
       count=count+1
       
print(count)    

