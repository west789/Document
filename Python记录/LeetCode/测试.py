class stu(object):
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 55
t = stu()
print(dir(t))
print(t.__baz)