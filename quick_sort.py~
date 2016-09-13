def quick_sort(A,p,r):
	if (p<r):
		q=partition(A,p,r)
		quick_sort(A,p,q-1)
		quick_sort(A,q+1,r)
	
	
def partition(A,p,r):
	i=p-1
	j=r+1
	pivot=A[int((p+r)/2)]
	
	while i<j:
		i+=1
		j-=1
		
		while A[i]<pivot:
			i+=1
		
		while A[j]>pivot:
			j-=1
		
		if i<j:
			temp=A[i]
			A[i]=A[j]
			A[j]=temp
	return j
			
a=[23,533,24,56,35,13,64,446,74]
quick_sort(a,0,len(a)-1)
print(a)
				
