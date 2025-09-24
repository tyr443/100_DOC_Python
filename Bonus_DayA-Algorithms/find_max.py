import random as rd

n = 5

nums = rd.sample(range(-101, 10), n)
print(nums)
biggest = nums[0]
pos = 0

for i in range(0, n):
    if nums[i] >= biggest:
        biggest = nums[i]
        pos = i

print(f"The biggest number is {biggest} at position {pos} in the array")
