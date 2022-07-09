def solution(programs):
    answer = 0
    used_tv = [0] * 25

    
    # 위 포문은 아래와같다.
    for p in programs:
        # print(p)# programs에 있는 1차원배열이 p에 담겨 옴.
        for i in range(p[0], p[1]): # for i in p는 두부분만 하니까
            # print(i)
            used_tv[i]+=1
    # print(used_tv)

    for i in used_tv:
        if i > 1:
            answer = answer + 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
programs = [[1, 6], [3, 5], [2, 8]]
ret = solution(programs)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")