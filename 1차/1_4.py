def func_a(arr):
    """
    가장 최대 길이만큼 0으로 리스트를 만들어두고
    매개변수로 오는 arr의 각 값을 인덱스번호로 하여 
    해당 인덱스 값을 증가시킴
    counter : arr의 각 값이 몇번 등장하는지 개수 저장
    어떤 값이 몇번 등장하는지도 인덱스 번호로 알 수 있지만 여기선 가장 많이 등장하는 숫자의 '개수'를 알고싶어하기에.
    """
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1

    # for x in arr:
    #     counter[x] = arr.count(arr[x])
    # 여기선 count함수를 아예 못쓸것 같다.
    # 코드 해석하면 x가 0일때 arr[0]의 값이 arr에 몇번 들어있는지 세어서 counter[0]에 저장하라. 근데 arr[1]==arr[0]이라면?
    # arr에 다 다른 값이 들어있으면 가능했을듯.

    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x: # 리스트 중 빈도수가 가장 적은 요소를 ret에 저장
            ret = x
    return ret

def func_c(arr):
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:  # x!=0을 꼭 확인해야할까?
            ret = x
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt # 몇 배인지 구하기(몫)
    # return int(max_cnt / min_cnt) # 나누고 정수만 가져오기

#The following is code to output testcase.
arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")