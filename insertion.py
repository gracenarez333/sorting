li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30, 1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]

def insertion_sort(li):
    for i in range(1, len(li)):
        j = i
        while(j > 0 and li[j - 1] > li[j]):
            li[j - 1], li[j] = li[j], li[j - 1]
            j -= 1

insertion_sort(li)
print(li)