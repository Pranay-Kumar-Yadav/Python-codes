#maximum sub array program 
def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


print("Maximum Subarray Program")


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

# ---- processing ----
result = maxSubArray(arr)

print("Maximum subarray sum:", result)

