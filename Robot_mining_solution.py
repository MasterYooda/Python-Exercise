from sys import stdin
import numpy as np
args = []
for line in stdin:
    args.append(line)

mn = args[0].split(" ")
nums = args[1].split(" ")
nums = [int(i) for i in nums]
m = int(mn[0])
n = int(mn[1])
print(m)
print(n)
nums = np.asarray(nums)
nums = nums.reshape((m,n))
print(nums)

results = np.zeros((m, n*n)) -1
results[0, n-1] = nums[0,0] + nums[0, n-1]

print(results)

for i in range(m-1):
    for j in range(n*n):
        if results[i,j] == -1:
            continue
        else:
            a = j//n
            b = j%n
            for k in range(3):
                for l in range(3):
                    if a-1+k > -1 and b-1+l > -1 and a-1+k < n and b-1+l < n:
                        if a-1+k != b-1+l:
                            results[i+1, (a-1+k)*n + b-1+l] = max(results[i+1, (a-1+k)*n + b-1+l], results[i, j] + nums[i+1, a-1+k]+nums[i+1, b-1+l])
                        else:
                            results[i+1, (a-1+k)*n + b-1+l] = max(results[i+1, (a-1+k)*n + b-1+l], results[i, j] + nums[i+1, a-1+k])    

print(results)
print("The desired maximum is: "+ str(results[m-1, n-1]))
