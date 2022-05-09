#!/usr/bin/python3
"""reducer.py"""

import sys



id2=None
current_follow=0
current_id=None
print('so luong theo doi la:')
    # đưa ra thiết bị xuất chuẩn các cặp <word, 1>, cách nhau bằng ký tự tab
for line in sys.stdin:
    
    
    id2, follow = line.strip().split('\t', 1)
    

    try:
        follow = int(follow)
    except ValueError:
        # nếu không phải giá trị số thì bỏ qua
        continue
    


# Ở cuối pha Map, các cặp (key, value) đã được sắp xếp theo key (ở đây là các từ).
    # Vì vậy ở pha Reduce, chương trình sẽ cộng giá trị value của dãy liên tiếp các từ trùng nhau
    # cho đến khi gặp từ mới.
    if id2 == current_id: # nếu từ mới trùng với từ đang xét thì tăng giá trị đếm của từ đang xét
        current_follow += follow
    else: 
        if current_id: # nếu gặp từ mới thì in ra số lần xuất hiện của từ đang xét
            print('%s\t%s' % (current_id, current_follow))
        # sau đó chuyển sang xử lý từ mới
        current_follow = follow
        current_id = id2
        
        

# in ra từ cuối cùng 
if current_id == id2:
    print('%s\t%s' % (current_id, current_follow))
