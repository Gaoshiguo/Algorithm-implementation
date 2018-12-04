def bubble_sort(arr):#定义一个冒泡排序算法
    i,j = 0,0#定义两个变量i,j,用来记录数组的范围，防止越界
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):#每一个j+1都是在原来已经排好序的数组中新加入的元素，将每一个第j+1元素与原来
            #已经排好序的数组中的元素比较
            #知道找到一个比这个新元素大的数，将新数与找到的这个数字交换
            if arr[j] >= arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]#交换
    return arr

alist=[69,3,2,45,67,3,2,4,45,63,24,233]
print(bubble_sort(alist))