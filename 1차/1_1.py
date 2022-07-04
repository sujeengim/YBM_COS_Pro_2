#You may use import as below.
#import math

def solution(shirt_size):
    """answer : shirt_size의 각 사이즈별 필요한 개수"""
    """answer를 필요한 길이만큼 0으로 채우고 값 수정하는 방법"""
    #Write code here.
    answer = []
    answer = [0 for _ in range(len(shirt_size))] # answer = [0]*6
    for i in shirt_size:
        if (i=='XS'):
            answer[0] += 1
        elif (i=='S'):
            answer[1] += 1
        elif (i=='M'):
            answer[2] += 1
        elif (i=='L'):
            answer[3] += 1
        elif (i=='XL'):
            answer[4] += 1
        else:
            answer[5] += 1
    return answer

def solution2(shirt_size):
    """answer가 빈 상태에서 값 추가하는 방법"""
    answer = []
    answer.append(shirt_size.count('XS'))
    answer.append(shirt_size.count('S'))
    answer.append(shirt_size.count('M'))
    answer.append(shirt_size.count('L'))
    answer.append(shirt_size.count('XL'))
    answer.append(shirt_size.count('XXL'))
    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")