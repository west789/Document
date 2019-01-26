class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.value_list = []
        self.main = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.value_list.append(x)
        if self.main == None or x <self.main:
            self.main = x
        

    def pop(self):
        """
        :rtype: void
        """
        pop_item = self.value_list.pop()
        if len(self.value_list) == 0:
            self.main = None
            return pop_item
        if pop_item == self.main:
            self.main = min(self.value_list)
        return pop_item
         

    def top(self):
        """
        :rtype: int
        """
        return self.value_list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.main

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-1)
    minStack.push(3)
    minStack.push(1)
    print(minStack.value_list)
    print(minStack.getMin())
    print(minStack.top())
    minStack.pop()
    print(minStack.top(), ":", minStack.value_list)