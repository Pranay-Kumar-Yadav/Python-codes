#partition equal subset sum
def canPartition(nums):
    total = sum(nums)

    #total sum is odd → impossible
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        # Traverse backwards
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    return dp[target]


# Test
nums = [1, 5, 11, 5]
print(canPartition(nums))