#!/usr/bin/python3
"""reducer.py"""
import sys
mutual_follow=[]
print('Liet ke tat ca cac cap nguoi dung theo doi lan nhau:')
    # đưa ra thiết bị xuất chuẩn các cặp <id1, id2>, cách nhau bằng ký tự tab
for line in sys.stdin:
    line = line.strip()
    id1, id2 = line.strip().split('\t', 1)
    mutual_follow.append((id1,id2))
    # Ở cuối pha Map, các cặp (key, value) đã được sắp xếp theo key (ở đây là các từ).
    # Vì vậy ở pha Reduce, chương trình sẽ cộng giá trị value của dãy liên tiếp các từ trùng nhau
    # cho đến khi gặp từ mới.
    if(len(mutual_follow)!=0) :
        if (id2,id1) in mutual_follow : # nếu từ mới trùng với từ đang xét thì tăng giá trị đếm của từ đang xét
	        print('%s\t%s' % (id1, id2))


