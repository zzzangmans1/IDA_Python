print("*** 섹션 출력 시작 ***")
print(" name\tstart\tend ")
for seg in Segments():
    print(idc.get_segm_name(seg), idc.get_segm_start(seg), idc.get_segm_end(seg))
print("*** 섹션 출력 끝 ***")
    
