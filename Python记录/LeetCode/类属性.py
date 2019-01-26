class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count = self.count+1
    
    @property
    def token(self):
        return self._token
    
    @token.setter
    def token(self, value):
        self._token = value

# print(Student.count)
# bart = Student('bart')
# print(Student.count)
# lisa = Student('lisa')
# print(Student.count)

#属性方法
student = Student('psl')
student.token = "this is a test toke"
print (student.token)