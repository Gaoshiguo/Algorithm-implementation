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

def buildheap(seq, size): #build heap
    for i in range(int(size / 2 )- 1, -1, -1):
        heapadjust(seq, i, size)

def heapsort(seq, size): # we can get the maximum value in each loop and put it at the end of array
    buildheap(seq, size)
    for j in range(size - 1, -1, -1):
        tem = seq[0]
        seq[0] = seq[j]
        seq[j] = tem
        buildheap(seq, j)
    return seq


if __name__ == '__main__':
    l = [0, 16, 20, 3, 11, 17, 8]
    print (heapsort(l, len(l)))