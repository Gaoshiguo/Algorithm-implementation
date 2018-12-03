def merge_sort(left,right):#这里定义合并函数，用来比较两个数组将最小的元素放在一个临时数组中
    i,j = 0,0#有两个变量i,j来控制左右两个数组的比较
    temp = []#定义一个存储数组，用来存放比较过的较小的按次序排列
    while i < len(left) and j < len(right):
        if left[i] < right[j]:#如果左边的第一个数比较小，将其放入存储数组，将左边的变量i向后移动以为，将左边第二个元素与右边第一个元素进行比较
            temp.append(left[i])
            i = i+1
        else:#如果右边的元素小，与上边情况类似
            temp.append(right[j])
            j = j+1
    if i >= len(left):#判断特殊情况：左边的数组已经比较完了，右边还有未比较的，直接使用append方法。将剩余右边的元素添加到数组中
        temp.extend(right[j:])
    if j >= len(right):#判断特殊情况：右边的数组已经比较完了，左边还有未比较的数，直接将左边的剩余数组加到temp数组中
        temp.extend(left[i:])
    return temp
def merge(arr):#定义切分函数，使用递归
    if len(arr) <=1:#当切分到数组中只有一个元素时，停止切分你
        return arr
    else:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        left = merge(l)#递归切分
        right = merge(r)#递归切分
    return merge_sort(left,right)#递归出口调用合并函数
alist=[69,3,2,45,67,3,2,4,45,63,24,233]
print(merge(alist))