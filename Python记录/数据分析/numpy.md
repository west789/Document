# numpy知识点
## 数组的形状
> 1. t=np.array(24).reshape(4, 6)  
t = np.flatten()   变为一维数组  


> 2. 广播机制  
*数组与数字相乘*   
*数组与数组相乘*

> 3.数据类型的操作  
b = random.random() 取小数
c = random.randint(4, 9)   
t1 = np.random.rand(2,3)创建一个2行3列的(0-1)随机数 
np.round(b, 2)   
np.argmax(t1,axis=1)返回每一行最大值的索引(位置)
np.argmin(t1,axis=0)返回每一列最小值的索引(位置)  
np.nan是float类型的  np.isnan(t3)  与 t3!=t3效果一样  
np.count_nonzero(t3!=t3)  t3[np.isnan(t3)]


> 4.数组索引和切片  
t1[:, :]前面是行，后面是列  
t2=t2[t2>10]  np.where(t2>10, 1, 0)  np.clip(10, 12) 小于10的赋值为10，大于12赋值为12  
a=b a=b[:]相互影响 浅复制  
a=b.copy()互不影响 深复制

> 4.inf 正无穷  
判断nan个数 np.count_nonzero(t2 != t2)   np.count_nonzero(np.isnan(t2))
> 5.vsplit hsplit vstack hstack  
vsplit和vstack相互可逆  np.vstack((t1,t2)) **平均分配**：(若不均报错)np.vsplit(t1,2) **不平均分割**:np.vsplit(t1,[1,2])(索引从1开始)  
hsplit和hstack相互可逆