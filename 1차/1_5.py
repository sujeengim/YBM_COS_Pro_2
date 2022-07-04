def solution(arr):
    """
    리스트 뒤집기
    왼쪽 인덱스와 오른쪽 인덱스 서로 바꾸기
    """
    left, right = 0, len(arr)-1
    while left<=right: # 조건 헷갈리지 않기
        arr[left], arr[right] = arr[right], arr[left]
        left += 1 
        right -= 1
    return arr

    # 다른 방법
    # arr2[] # 새 리스트를 만들어서
    # for i in range(len(arr)-1,-1,-1): # 0~len(arr)과 같은 길이인 len(arr)-1~-1만큼 반복한다. 스텝은 -1
    #     arr2.append(arr[i]) #arr2의 뒷 인덱스부터 arr의 앞인덱스 값이 채워진다.

#이건 왜 안될까
def reverse2(arr):
    arr = arr.reverse()
    return arr

#The following is code to output testcase.
arr = [1, 4, 2, 3]
ret = solution(arr)
ret2 = reverse2(arr)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .", ret2)