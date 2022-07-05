def solution(characters):
    result = "" 
    result += characters[0] # characters의 첫번째 문자를 담아서 두 번째 문자와 같은지 비교하기
    for i in range(1, len(characters)):
        if characters[i - 1] != characters[i]: #인덱스는 0번부터 시작하는데 -1하면 음수되니까 1번부터 시작하도록.
            result += characters[i]
    return result

#The following is code to output testcase. The code below is correct and you shall correct solution function.
characters = "senteeeencccccceeee"
ret = solution(characters)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")