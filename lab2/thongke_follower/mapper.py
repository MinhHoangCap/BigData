#!/usr/bin/python3
"""mapper.py"""

import sys

# Chương trình Python chạy trên Hadoop MapReduce qua tính năng Streaming.
# Dữ liệu vào từ thiết bị nhập chuẩn (STDIN)
# Kết quả xử lý gửi ra thiết bị xuất chuẩn (STDOUT)



for line in sys.stdin.buffer.raw:
    line = line.strip()
    id1,id2=line.split()#bor ky tu trang o dau va cuoi, tach cac chuoi ra
    # loại bỏ ký tự trắng ở đầu và cuối chuỗi
    print('%s\t%s' % (id2, 1))

