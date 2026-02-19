def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)

    return result


print("Monotonic Stack Program")

n = int(input("Enter number of elements: "))

nums = []

# 🔹 INPUT happening in the middle of execution
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    nums.append(num)

print("Input array:", nums)

result = next_greater_element(nums)

print("Next Greater Elements:", result)


