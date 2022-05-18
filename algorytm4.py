def partition(low, high, arr):
	pivot = arr[high]
	ptr = low
	for i in range(low, high):
		if arr[i] <= pivot:
			arr[i], arr[ptr] = arr[ptr], arr[i]
			ptr += 1
	arr[ptr], arr[high] = arr[high], arr[ptr]
	return ptr

def quicksort(low, high, arr):
	if len(arr) == 1: 
		return arr
	if low < high:
		pivotIdx = partition(low, high, arr)
		quicksort(low, pivotIdx-1, arr) 
		quicksort(pivotIdx+1, high, arr) 
	return arr
temp = [1,7,3,5,]
print("zad1")
print(temp)
print(quicksort(0, len(temp)-1, temp))

def permutacja(tabA,tabB):
    if len(tabA)!=len(tabB):
        return False
    for a in range(0,len(tabA)):
        for b in range(0,len(tabB)):
            if tabA[a]==tabB[b]:
                del tabB[b]
                break
    if len(tabB)!=0:
        return False
    return True
arra = [1,7,3]
arrb = [1,3,7]
print("zad2")
print(permutacja( arra,arrb))
arrb = [1,2,3]
print(permutacja( arra,arrb))