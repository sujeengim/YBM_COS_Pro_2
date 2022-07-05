def solution(number):
    """count : 1~number까지 박수친 횟수"""
    count = 0
    for i in range(1, number + 1):
        current = i
        temp = count

        while current != 0: # 10의자리 이상부터 369의 개수가 두개이상이 되기에 그거 확인하는 작업
            if current%10==3 or current%10==6 or current%10==9: # 현재 숫자의 일의자리가 369면. 문자가 아니라서 따옴표 없음.
                count += 1 # 369일 경우 count 변화
                print("pair", end = '') #369면 숫자대신 짝
            current = current // 10 # current가 1의 자리라면 여기서 0이 되면서 반복을 멈춤
        
        if temp == count: # 반복문을 거쳤는데 거치기 전과 같다면 369가 나오지 않았다는 의미
            print(i, end = '') #369 아니면 숫자 출력
        print(" ", end = '') 
    print("")
    return count

#The following is code to output testcase.
number = 40
ret = solution(number)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")