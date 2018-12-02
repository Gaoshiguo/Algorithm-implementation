def Insert_sort(arr):
    #第二种算法思想是，将新插入的元素从后往前依次比较，找到相应的位置，用变量a
    #来记录应当插入的位置。然后再把该位置之后的元素全部向后移动一位，前面的元素不动
    for i in range(1,len(arr)):
        a, b = i, i#用变量a,b来记录新插入元素的位置
        key = arr[i]
        while key < arr[a-1] and a-1>=0:
            a = a-1#找到应该插入的元素的位置
            if a-1 < 0:#当新插入的元素是最小的时候跳出循环
                a=0
        while b>a:#将插入的位置之后的元素全部向后移动一位
            arr[b] = arr[b-1]
            b = b-1
        arr[a] = key#将新插入的元素插在相应的位置上
l = [56,12,55,89,87,59]
Insert_sort(l)
print(l)
