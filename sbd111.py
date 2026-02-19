#longest increasing subsequence LIS
def length_of_lis(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


nums = list(map(int, input("Enter numbers: ").split()))
print("Length of LIS:", length_of_lis(nums))
