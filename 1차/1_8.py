def solution(sentence):
    str = '' # 알파벳만 담기
    for c in sentence:
        if c != '.' and c != ' ':
            str += c
    size = len(str)
    for i in range(size // 2): # 짝수면 딱 맞아떨어지고, 홀수면 가운데 혼자 남음.
        if str[i] != str[size - 1 - i]: # 순서대로인 str과 순서반대인 str이 서로 다르면 false 반환
            return False
    return True


#The following is code to output testcase. The code below is correct and you shall correct solution function.
sentence1 = "never odd or even."
ret1 = solution(sentence1)

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
sentence2 = "palindrome"
ret2 = solution(sentence2)

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")