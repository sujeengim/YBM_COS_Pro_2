def solution(number):
    count = 0
    while number > 0: #7번째 줄이 0보다 클때까지. 또는 0이 아닐때까지(True일때까지)
        n = number % 10 #가장 오른쪽 숫자를 n에 담기
        if n == 2 or n == 3 or n == 5 or n == 7:
            count += 1
        number //= 10 #가장 오른쪽 숫자 뺀 나머지 숫자 number에 담기
    return count

# 풀코딩(어디가 잘못된걸까)
def solution2(number):
    count=0
    strNum = str(number)
    for i in range(len(strNum)):
        print(i)
        if number[i]==2 or number[i]==3 or number[i]==5 or number[i]==7:
            count+=1 
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
number = 29022531
ret = solution(number)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

