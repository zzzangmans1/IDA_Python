byte = '80 38 cc ' #'55 8B EC'  PUSH ebp 찾을 바이트 입력
addr = ida_ida.inf_get_min_ea() # 최소 주소를 addr에 넣는다.
print("*** 80 38 cc 바이트 찾기 시작 ***")
for x in range(0, 10):
    addr = idc.find_binary(addr, SEARCH_DOWN | SEARCH_NEXT, byte)
    if addr != idc.BADADDR:
        print( x, hex(addr), idc.GetDisasm(addr))
print("*** 80 38 cc 바이트 찾기 끝 ***")
