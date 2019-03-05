def new_tips(arg):
    def tips(func):
        def nei(a, b):
            print("start %s" %arg)
            func(a,b)
            print("stop")

        return nei
    return tips

@new_tips("add")
def add(a, b):
    print(a+b)

add(3,5)
# add = tips(add)
# print(type(add))
# add(3,5)