print("*** 87 05 ***")
print("*** 바이트 찾기 시작 ***")
addr = ida_ida.inf_get_min_ea() # 시작 주소
byte = "87 05" # xchg 
cnt = 1
while(addr < ida_ida.inf_get_max_ea()):
    addr = idc.find_binary(addr, SEARCH_DOWN | SEARCH_NEXT, byte)
    if addr != idc.BADADDR :
        print("%d addr\tasm" % cnt)
        print(hex(addr), idc.GetDisasm(addr))
        for i in range(22) :
            ida_bytes.patch_byte(addr+i, 0x0) # 주소의 바이트를 0으로 변경
        cnt+= 1
print("*** 바이트 패치 끝 ***")
