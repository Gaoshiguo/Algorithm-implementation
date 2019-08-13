
# 堆排序算法分为大根堆排序和小根堆排序。我们选择一种学会即可
## 堆排序一般分为两步，首先是建一个堆，然后再依据相应的要求将堆调整为大（小）根堆。因此整个算法也就分成两个部分
* buildheap和heapadjust，这两个函数分别完成建堆和调整堆的操作
```python
def buildheap(seq, size): #build heap
    for i in range(int(size / 2 )- 1, -1, -1):
        heapadjust(seq, i, size)
```
在建堆的过程中同时调整节点的位置
heapadjust函数采用递归调用，每一次比较根节点与其左右子树的值，调整结构
```python
def heapadjust(seq, node, size): #adjust heap
    lchild = 2 * node + 1
    rchild = 2 * node + 2
    maxcode = node
    if node <= size / 2 - 1: #if lefthchild or rightchild > root node, exchange the value
        if lchild <= size - 1 and seq[lchild] > seq[maxcode]:
            maxcode = lchild
        if rchild <= size - 1 and seq[rchild] > seq[maxcode]:
            maxcode = rchild
        if maxcode != node:
            tem = seq[node]
            seq[node] = seq[maxcode]
            seq[maxcode] = tem
            heapadjust(seq, maxcode, size) #adjust the heap which root is maxcode
 ```
 


