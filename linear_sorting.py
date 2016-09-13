import random

class linear_sorting:

    def __init__(self,array):
        self.array=array

    def counting_sort(self,b):

        max_item=max(self.array)
        store=[0]*(max_item+1)

        for x in self.array:
            store[x]+=1

        for i in range(2,len(store)):
            store[i]+=store[i-1]

        count=1;

        for x in self.array:
            b[(store[x])-1]=x
            store[x]-=1
            print ('\nPass %d\n'%count)
            print(b)
            print("\n")
            count+=1
        return b

    def radix_sort(self,b):

        copy=[0]*len(self.array)

        for num in range(len(copy)):
                copy[num]=self.array[num]

        max_item=max(self.array)
        d=len(str(max_item))

        for j in range(d):

            for num in range(len(copy)):
                copy[num]=copy[num]%10

            max_item=max(copy)
            store=[0]*(max_item+1)

            for x in copy:
                store[x]+=1

            for i in range(1,len(store)):
                store[i]+=store[i-1]

            count=len(self.array)-1
            for t in range(len(copy)-1,-1,-1):
                b[(store[copy[t]]-1)]=self.array[count]
                store[copy[t]]-=1
                count-=1

            for q in range(len(self.array)):
                self.array[q]=b[q]

            print ('\nPass %d'%j)
            print(b)
            print("\n")

            for i in range(len(copy)):
                copy[i]=int(b[i]/pow(10,j+1))

        return b

class bucket_sort:

    def __init__(self,data=None):
        self.data=data
        self.next=None

    def sort(self,a,b):

        max_size=int((max(a))/(len(a)))
        bucket=bucket_sort()
        copy=[]

        for i in range(max_size+2):
            copy.append(bucket_sort())
        ptr=bucket_sort()
        temp=bucket_sort()
        for i in range(len(a)):
            rem=int(a[i]/(len(a)))
            ptr=copy[rem]
            if (ptr.data==None):
                ptr.data=a[i]
                ptr.next=None

            else:
                while (ptr.data!=None):
                    if (ptr.data<a[i]) & (ptr.next!=None):
                        ptr=ptr.next
                    elif (ptr.data<a[i]) & (ptr.next==None):
                        bucket=bucket_sort(a[i])
                        ptr.next=bucket
                        bucket.next=None
                        break
                    else:
                        temp=ptr.next
                        bucket=bucket_sort(ptr.data)
                        ptr.next=bucket
                        bucket.next=temp
                        ptr.data=a[i]
                        break

        count=0
        for j in range(len(copy)):
            ptr=copy[j]
            while (ptr!=None):
                if ptr.data!=None:
                    b[count]=ptr.data
                    count+=1

                ptr=ptr.next

        return(b)


def run():

    my_array=[]
    limit=10
    for num in range(limit):
            my_array.append(random.randrange(150,160))

    print("Array\n------------------------")
    print(my_array)
    print("-------------------------------")


    ex=linear_sorting(my_array)
    bucket=bucket_sort()

    res=[0]*limit
    '''ex.radix_sort(res)

    '''
    ch=0
    while(ch!=4):
        print ("0.New array")
        print ("1.Counting Sort")
        print ("2.Radix Sort")
        print ("3.Bucket Sort")
        print ("4.Exit\n")
        ch=int(input())

        if ch==0:
            my_array=[]
            for num in range(limit):
                my_array.append(random.randrange(100,200))

            print("Array\n------------------------")
            print(my_array)
            print("-------------------------------")


            ex=linear_sorting(my_array)
            bucket=bucket_sort()

        elif ch==1:
            ex.counting_sort(res)
            print("\nSorted Array\n------------------------")
            print(res)
            print("\n")

        elif ch==2:
            ex.radix_sort(res)
            print("\nSorted Array\n------------------------")
            print(res)
            print("\n")

        elif ch==3:
            bucket.sort(my_array,res)
            print("\nSorted Array\n------------------------")
            print(res)
            print("\n")

        elif ch==4:
            print("You choose to exit !!!")
            print("\n")

        else:
            print("What's that again ???")
            print("\n")

run()








