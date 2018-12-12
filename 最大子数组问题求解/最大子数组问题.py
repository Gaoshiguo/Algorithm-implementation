def baoli(arr):#方法一暴力解决，该方法比较简单，不做过多解释
    maxsum = arr[0]
    list = []
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            tempsum = 0
            for k in range(i,j):
                tempsum = tempsum+arr[k]
            if tempsum >= maxsum:
                maxsum = tempsum
    print(maxsum)


def find_across(arr,left,right):#方法二是基于分治法的思想：最大子数组的出现只可能有三种情况
    #完全位于左半部分；完全位于右半部分；跨越左右半部分。跨越的子数组情况比较特殊，我们先来找出跨越子数组如何来进行寻找
    #首先将数字分成两个部分，我们先查找跨越的最大子数组
    leftmax = -float('inf')##将leftmax赋值为负无穷大，在python中，-float（"inf"）代表赋值负无穷
    #float("inf")代表赋值为无穷大
    rightmax = -float('inf')#将rightmax也赋值为负无穷大
    #我们可以将leftmax和rightmax理解为两个变量，用来记录左半边和右半边在计算时
    #的值，记录做半边的半截数组中连续加起来值最大的子数组的值；
    ileft = -float('inf')#ileft可以理解为记录数组游标的一个变量，用来存储
    #得到最大子数组时的一个数组坐标
    iright = -float('inf')
    list_1 = []#定义一个空的数组来存储最终得到的最大子数组的值，以及子数组的坐标
    sum = 0#定义一个变量用来存储计算得到的最大子数组的值
    mid = (left+right)//2
    for i in range(mid,left-1,-1):#左半边，从中间位置开始，依次向前加，并记录最大的子数组的值
        sum = sum+arr[i]
        if sum > leftmax:
            leftmax = sum
            ileft = i#记录在更新sum值时的坐标
    sum = 0
    for j in range(mid+1,right,1):
        sum = sum + arr[j]
        if sum > rightmax:
            rightmax = sum
            iright = j
    list_1 = [leftmax+rightmax,ileft,iright]#leftmax+rightmax为最大子数组的值，ileft,iright为起始最大子数组的游标
    return list_1
def find_all(arr,left,right):
    if left==right:
        maxlist = [arr[left],left,right]
        return maxlist
    else:
        l = []
        r = []
        m = []
        mid = (left+right)//2
        l = find_all(arr,left,mid)
        r = find_all(arr,mid+1,right)
        m = find_across(arr,left,right)
        if l[0]>=r[0] and l[0]>=m[0]:
            return l
        elif r[0]>=l[0] and r[0]>=m[0]:
            return r
        else:
            return m
arr = [1,8,9,-5,-3,-1,-3]
print(find_all(arr,0,len(arr)-1))