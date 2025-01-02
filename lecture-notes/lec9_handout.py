def bsearch(s, e, first, last, calls):
    print(first, last, calls)
    if (last - first) < 2:
        return s[first] == e or s[last] == e
    mid = int(first + (last - first)/2)
    if s[mid] == e:
        return True
    if s[mid] > e:
        return bsearch(s, e, first, mid-1, calls+1)
    return bsearch(s, e, mid + 1, last, calls+1)

def search1(s, e):
    print(bsearch(s, e, 0, len(s) -1, 1))
        
def selSort(L):
    for i in range(len(L) - 1):
        print(L)
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j = j + 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp
    
def testSelSort():
    test1 = [1,6,3,4,5,2]
    input('run selective test 1')
    selSort(test1)
    test2 = [6,1,2,3,4,5]
    input('run selective test 2')
    selSort(test2)
    test3 = [6,5,4,3,2,1]
    input('run selective test 3')
    selSort(test3)
    test4 = [1,2,3,4,5,6]
    input('run selective test 4')
    selSort(test4) 
    
# def bubbleSort(L):
#     for j in range(len(L)):
#         for i in range(len(L)-1):
#             if L[i] > L[i+1]:
#                 temp = L[i]
#                 L[i] = L[i+1]
#                 L[i+1] = temp
#         print(L)
        
def bubbleSort(L):
    swapped = True
    while swapped:
        swapped = False
        print(L)
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                swapped = True

def testBubbleSort():
    test1 = [1,6,3,4,5,2]
    input('run bubble test 1')
    bubbleSort(test1)
    test2 = [6,1,2,3,4,5]
    input('run bubble test 2')
    bubbleSort(test2)
    test3 = [6,5,4,3,2,1]
    input('run bubble test 3')
    bubbleSort(test3)
    test4 = [1,2,3,4,5,6]
    input('run bubble test 4')
    bubbleSort(test4)
 
 
if __name__ == "__main__":
    # testSelSort()
    testBubbleSort()