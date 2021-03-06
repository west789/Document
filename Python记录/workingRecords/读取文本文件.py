import os
# def read_bike(path):
#     with open(path, 'r+', encoding="utf-8") as f:
#         # data3 = f.read()
#         # data = f.readline()
#         for line in f:
#             print(line)
#         # data1 = f.readline()
#         while True:
#             line = f.readline()
#             if not line:
#                 break
#             print (line)
        
#         data2 = f.readline()
        
#         # print(data, data1, data2)
#     path_new = os.path.join(os.path.dirname(__file__), "bike2.txt")
#     print(path_new)
#     with open(path_new, 'w+', encoding="utf-8") as fw:
#         list2 = ["11", "22", "33"]
#         list2 = map(lambda item: item+"\n", list2)
#         fw.writelines(list2)

# path1 = os.path.dirname(os.path.dirname(__file__))
# print (__file__)
# path = os.path.join(os.path.dirname(__file__), "bike.txt")
# print (path)
# read_bike(path)

# def read_in_block(path):
#     BLOCK_SIZE = 1024
#     with open(path, 'r', encoding='utf-8') as f:
#         while True:
#             block = f.read(BLOCK_SIZE)
#             if block:
#                 yield block
#             else:
#                 break

# path = os.path.join(os.path.dirname(__file__), 'bike.txt')
# for block in read_in_block(path):
#     print(block)
def read_in_chunks(file_obj, chunk_size = 2048):
    """
    逐件读取文件
    默认块大小：2KB
    """
    while True:
        data = file_obj.read(chunk_size)  # 每次读取指定的长度
        if not data:
            break
        yield data

with open('filename', 'r', encoding = 'utf-8') as f:
    for chuck in read_in_chunks(f):
        do_something(chunk)
