#climbing stairs
def climb_stairs(n):
    if n <= 2:
        return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)


n = int(input("Enter number of steps: "))
print("Number of ways:", climb_stairs(n))
