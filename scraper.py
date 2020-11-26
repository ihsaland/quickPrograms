def sumPairs(arr, s):
    stack = []
    count = 0
    for i in range(0, len(arr)):
        stack.append(i)
        for j in range(i + 1, len(arr)):
            if j in stack:
                break
            if arr[i] + arr[j] == s:
                count += 1
                print(arr[i]," + ",arr[j],"=",s)

    if count == 0:
        print("no pairs found that equal:",s)




if __name__ == '__main__':
    arr = [1,4,45,6,10,-8,1]
    s = 14

    sumPairs(arr,s)