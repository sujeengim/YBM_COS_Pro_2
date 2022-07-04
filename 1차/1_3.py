def func_a(month, day):
    """
    푼 방법 : 반복변수가 범위내 month_list의 각 값을 담고 그 값을 total에 누적
    주석 방법 : 범위만큼 반복하면서 total에서 month_list의 각 값을 가져와 누적하는 방법
    """
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in month_list[:month-1]:
        total += i
    # for i in range(month-1):
    #     total += month_list[i]
    total += day
    return total - 1
        
def solution(start_month, start_day, end_month, end_day):
    """1월1일부터 끝날짜의 거리 - 1월1일부터 시작날짜의 거리를 반환"""
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total

#The following is code to output testcase.
start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")