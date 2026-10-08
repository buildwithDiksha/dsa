arr = [2,4,1,7,3,6]
k=3
window_sum = 0
for i in range(k):
    window_sum=window_sum+arr[i]
print(window_sum)

for i in range(k,len(arr)):
    window_sum_sum=window_sum-arr[i-k]+arr[i]
    print(window_sum_sum)    

