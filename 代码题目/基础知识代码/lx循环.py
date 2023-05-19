一、for循环作业
1：输出99乘法表
for i in range(1,10):
for j in range(1,i+1):
print('%d*%d=%d'%(i,j,i*j),end = ' ' )
print()


3：有1,2,3,4这四个数字，能组成多少个互不相同且无重复数字的三个数？分别是什么？
提示：123，321就是符合要求，数字既不相同，而且每个数字的个十百位也不重复；而121,212就不行，因为数字的各位与百位重复
list = [1, 2, 3, 4]
count = 0
for a in list:
    for b in list:
        for c in list:
            if (a != b) and (a != c) and (b != c):
                count += 1
                print(a, end="")
                print(b, end="")
                print(c, end=" ")
print("")
print("共计%d个结果" % count)


4：请用嵌套for循环输入如下直角三角形
*
**
***
****
*****
for i in range(1,5):
        print('*'*i)


5：请用嵌套for循环输出如下等边三角形（三个边均是5个*）
*
* *
* * *
* * * *
* * * * *
for Index_row in range(1,6):

    for index_space in range(1,6-Index_row):
        print(" ",end="")

    for Index_col in range(1,Index_row+1):
        print("* ",end="")
    print()

四、for..range练习：

1：利用for循环和range找出 0 ~ 100 以内所有的偶数，并追加到一个列表。
list1 = []
for i in range(0,100,2):
    list1.append(i)
print(list1)

2：利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。
list2 = []
for j in range(0,50):
    if j%3 ==0:
        list2.append(j)
print(list2)

3：利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：
[48,45,42...]
list3 = []
for k in range(0,50):
    if k%3 == 0:
        list3.insert(0,k)
print(list3)

4：查找列表li中的元素，移除每个元素前后的空格，并找出以”a”开头的元素，添加到一个新列表中,最后循环打印这个新列表。
li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
li1 = []
for m in li:
    b = m.strip().startswith('a')
    if b == True :
        li1.append(m.strip())
for n in li1:
    print(n)