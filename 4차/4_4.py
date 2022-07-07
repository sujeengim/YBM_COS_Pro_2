'''
교실별 학생수 classes, 조교한명당담당학생수 m
수업 진행 위한 조교 수 return
'''

def solution(classes, m):
    answer = 0
    for students in classes:
        answer += students // m
        if students % m != 0:
            answer += 1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
classes = [80, 45, 33, 20]
m = 30
ret = solution(classes, m)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")