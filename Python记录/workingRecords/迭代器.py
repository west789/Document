# class MyNumber:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         if self.a<=3:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration

# num = MyNumber()
# numiter = iter(num)
# print(next(numiter))
# print(next(numiter))
# print(next(numiter))
# print(next(numiter))
# for i in numiter:
#     print(i)
# def Fibnacci(n):
#     a, b, counter = 0, 1, 0
#     while counter<=n:
#         yield a
#         a, b = b, a+b
#         counter += 1

# for i in Fibnacci(10):
#     print(i)

def new1_out(c, d):
    def addNew1(func):
        def internel(a, b):
            print("addNew1-----")
            print(c+d)
            func(a,b)
            print("over new1")
        return internel
    return addNew1
def addNew(func):
    def internel(a, b):
        print("do something")
        func(a, b)
        print("do nothing")
    return internel

@new1_out(6, 8)
@addNew
def add(a, b):
    print(a+b)

add(3,4)