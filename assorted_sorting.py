import random

count_merge=0
count_quick=0
count_heap=0

'''--------------------------------------------------------------------------'''

class assorted_sorting:

    def __init__(self,limit):
        self.limit=limit
        self.array=[]
        self.count_bubble=0
        self.count_selection=0
        self.count_merge=0
        self.count_quick=0
        self.count_bucket=0
        self.count_heap=0
        for num in range(limit):
            self.array.append(random.randrange(1,100))

    def get_output_bubble(self):
        return self.count_bubble
    def get_output_selection(self):
        return self.count_selection
    def get_output_merge(self):
        return self.count_merge
    def get_output_quick(self):
        return self.count_quick
    def get_output_bucket(self):
        return self.count_bucket
    def get_output_heap(self):
        return self.count_heap

    def bubble_sort(self):

        for num in range(self.limit):
            for in_num in range(num+1,self.limit):
                if self.array[num]>self.array[in_num]:
                    self.count_bubble+=1

    def selection_sort(self):

        temp=0
        for num in range(self.limit):
            temp=self.array[num]
            for num_in in range(num+1,self.limit):
                if self.array[num_in]>temp:
                    self.count_selection+=1

    def merge_sort(self):

        global count_merge
        count_merge=0
        arr=mergesort(self.array)
        self.count_merge=count_merge

    def quick_sort(self):

        global count_quick
        count_quick=0
        arr=quicksort(self.array)
        '''print(arr)'''
        self.count_quick=count_quick

    def bucket_sort(self):

        max_item=max(self.array)
        result=[]
        store=[0]*(max_item+1)

        for x in self.array:
            store[x]+=1
            self.count_bucket+=1

        for x in range(max_item+1):
            self.count_bucket+=1
            if store[x]>0:
                result.append([x+1]*store[x])


    def heap_sort(self):
        global count_heap
        arr=[]
        for num in range(self.limit):
            count_heap+=1
            arr.append(self.array[num])
            heapify(arr,num+1)

        n=self.limit-1
        while n>0:
            count_heap+=1
            temp=arr[0]
            arr[0]=arr[n]
            arr[n]=temp
            n-=1
            shift_down(arr,0,n)
        self.count_heap=count_heap
        
'''--------------------------------------------------------------------------'''

def mergesort(lst):

    global count_merge
    if len(lst) <= 1:
        count_merge+=1
        return lst
    count_merge+=1
    middle = int(len(lst) / 2)
    left = mergesort(lst[:middle])
    right = mergesort(lst[middle:])
    return merge(left, right)

def merge(left, right):

    global count_merge
    count=0
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
            count_merge+=1
        else:
            result.append(right[j])
            j += 1
            count_merge+=1
    result += left[i:]
    result += right[j:]
    count_merge+=1
    return result

'''-------------------------------------------------------------------------'''

def quicksort(list):

    global count_quick
    left=[]
    right=[]
    if list == []:
        count_quick+=1
        return []
    else:
        count_quick+=1
        pivot = list[0]
        for x in list[1:]:
            if x<pivot:
                left.append(x)
                count_quick+=1
            else:
                right.append(x)
                count_quick+=1
        lesser = quicksort(left)
        greater = quicksort(right)
        return lesser + [pivot] + greater

'''--------------------------------------------------------------------------'''

def heapify(array,n):
    global count_heap
    '''count_heap+=1'''		
    for num in range(1,int(n/2)):
        p=int(n/2)
        temp=0
        if p>=1:
            if array[n-1]>array[p-1]:
                temp=array[n-1]
                array[n-1]=array[p-1]
                array[p-1]=temp
                heapify(array,p)
        else:
            return

def shift_down(array,parent,n):
    global count_heap
    count_heap+=1
    child=(2*parent)+1
    if child>=n:
        return
    if array[child+1]>array[child]:
        child+=1
    if array[child]>array[parent]:
        temp=array[child]
        array[child]=array[parent]
        array[parent]=temp
    shift_down(array,child,n)
    return

'''--------------------------------------------------------------------------'''
def run(n):

    sort_array=[]
    for num in range(n):
        sort_array.append(assorted_sorting((num+1)*100))

    f=open('store.xls','w')
    f.write('N\tBubble sort\tSelection sort\tMerge Sort\tQuick Sort\tHeap Sort\tBucket Sort\n')

    for num in range(n):

        sort_array[num].bubble_sort()
        sort_array[num].selection_sort()
        sort_array[num].merge_sort()
        sort_array[num].quick_sort()
        sort_array[num].bucket_sort()
        sort_array[num].heap_sort()

        output1=sort_array[num].get_output_bubble()
        output2=sort_array[num].get_output_selection()
        output3=sort_array[num].get_output_merge()
        output4=sort_array[num].get_output_quick()
        output5=sort_array[num].get_output_bucket()
        output6=sort_array[num].get_output_heap()

        f.write('%d\t'%((num+1)*100))

        f.write('%d\t'%output1)
        f.write('%d\t'%output2)
        f.write('%d\t'%output3)
        f.write('%d\t'%output4)
        f.write('%d\t'%output6)
        f.write('%d\n'%output5)

    f.close()

'''--------------------------------------------------------------------------'''

run(15)
'''a=assorted_sorting(10)
a.heap_sort()'''







