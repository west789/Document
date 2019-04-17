def Judge_A_superset_B(a, b):
    """
    1.遍历a字符串，将a字符串以元素及出现个数为key，value插入字典中
    2.遍历b字符串，将按照b字符串依次从a字符串中减去相应元素个数
    3.若b中的字符串不存在与a，则直接返回false
    时间复杂度为O(n)其中n为a的长度
    空间复杂度：因为使用的是字典，总体而言是O(n),n为a的长度
    """
    #a长度小于b长度直接返回非超集
    if len(a)<len(b):
        return False
    a_dict = {}
    #遍历a字符串，将a字符串以字典方式存入，如{"a":1, "b":2}
    for i in range(len(a)):
        a_dict[a[i]] = a_dict.get(a[i], 0)+1
    for j in range(len(b)):
        if not a_dict.get(b[j], 0) or a_dict.get(b[j]) <=0:
            return False
        else:
            a_dict[b[j]] -= 1
    return True
a = "abbccd"
b = "abcdd"
print(Judge_A_superset_B(a, b))