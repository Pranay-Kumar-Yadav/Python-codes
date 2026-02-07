#double sided staircase pattern
n = 10
for i in range(1, n + 1):
    k = i + 1 if i % 2 != 0 else i

    #print spaces before stars
    for g in range(k, n):
        print(end=" ")

        #print stars in each row
        for j in range(k):
            if j == k - 1:
                print(" * ")
            else:
                print(" * ", end=" ")