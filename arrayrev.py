def arrayRev(array):
    length = len(array)
    revArray = []
    i=length-1
    while i >= 0:
        revArray.append(array[i])
        i-=1
    return revArray

if __name__=="__main__":
    array = map(int,input().split())
    array = list(array)
    result = arrayRev(array)
    print(result)
