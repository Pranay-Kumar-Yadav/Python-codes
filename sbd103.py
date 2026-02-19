#top k elements
import heapq

def top_k_elements(arr, k):
    return heapq.nlargest(k, arr)


arr = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter value of k: "))

print("Top", k, "elements:", top_k_elements(arr, k))
