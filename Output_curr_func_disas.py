# 현재 함수 디스어셈블 출력 소스

ea = here()
#idc.get_func_name 함수는 주소를 넣으면 함수 이름반환 함수
print("Functions Name : "+idc.get_func_name(ea))
# get_func_attr에 인자값으로 FUNCATTR_START를 넣으면 1번째 인자값의 주소의 함수 시작 주소
# FUNCATTR_END를 넣으면 끝 주소
start = idc.get_func_attr(ea, FUNCATTR_START)
end = idc.get_func_attr(ea, FUNCATTR_END)
cur_addr = start
while cur_addr <= end:
    print(hex(cur_addr), GetDisasm(cur_addr))
    cur_addr = idc.next_head(cur_addr, end)
