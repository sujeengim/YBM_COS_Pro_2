def solution(num_apple, num_carrot, k):
    answer = 0
    
    # 일단 최대로 만들 수 있는 주스를 answer에 저장
    if num_apple < num_carrot * 3:
        answer = num_apple // 3
    # if num_apple//3>num_carrot:
    #     answer = num_carrot
    else:
        answer = num_carrot    

    # 남은 사과와 당근 개수 저장
    num_apple -= answer * 3
    num_carrot -= answer


    i = 0
    while k - (num_apple + num_carrot + i) > 0:
        if i % 4 == 0: # 4개당 한번씩 주스를 제거
            answer += 1
        i = i + 1
        
    return answer

    # 이렇게 바꿀 수 있음.
    # while (k > num_apple + num_carrot + i):
    #     answer -= 1
    #     i += 4
    # return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
num_apple1 = 5
num_carrot1 = 1
k1 = 2
ret1 = solution(num_apple1, num_carrot1, k1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num_apple2 = 10
num_carrot2 = 5
k2 = 4
ret2 = solution(num_apple2, num_carrot2, k2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")


#다른 방법

if num_apple//3 < num_carrot:
        answer = num_apple // 3
    else:
        answer = num_carrot

    num_apple -= answer * 3
    num_carrot -= answer

    i = 0
    while k > (num_apple + num_carrot +i) :
         answer -= 1
         i += 4
