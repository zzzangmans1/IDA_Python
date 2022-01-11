# 함수 목록 출력
print("*** 함수 목록 출력 시작 ***")
for func in Functions(): # 함수들 하나씩 가져와 func에 넣는다.
    print(hex(func)+ " : "+idc.get_func_name(func)) # 주소값으로 출력하고 함수 이름 으로출력
print("*** 함수 목록 출력 끝 ***")
