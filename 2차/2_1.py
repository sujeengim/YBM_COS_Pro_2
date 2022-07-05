max_product_number = 10

def func_a(gloves):
    counter = [0 for _ in range(max_product_number + 1)] #0 11개 채우기 : 아마 0번 인덱스는 비워둘 생각인듯
    for x in gloves:
        counter[x]+=1 #제품번호와 같은 번호의 인덱스에 1추가
    return counter

def solution(left_gloves, right_gloves):
    left_counter = func_a(left_gloves)
    right_counter = func_a(right_gloves)
    
    total = 0
    for i in range(1, max_product_number + 1):  #1부터 시작하고 있음. 인덱스번호0은 비워둔게 확실함.
        total += min(left_counter[i], right_counter[i])
    return total

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
left_gloves = [2, 1, 2, 2, 4]
right_gloves = [1, 2, 2, 4, 4, 7]
ret = solution(left_gloves, right_gloves)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")