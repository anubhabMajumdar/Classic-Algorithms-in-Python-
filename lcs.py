class lcs:

	def __init__(self,x,y):
		
		self.x=x
		self.y=y
		
		m=len(x)
		n=len(y)
		
		self.c=[]
		self.b=[]
		
		for i in range(m+1):
			new_c=[]
			new_b=[]
			for j in range(n+1):
				new_b.append("")
				new_c.append(0)
				
			self.c.append(new_c)
			self.b.append(new_b)
			
		
	def lcs_compute(self):
		
		m=len(self.x)
		n=len(self.y)
		
		for i in range(m+1):
			self.c[i][0]=0
		
		for i in range(n+1):
			self.c[0][i]=0
			
		for i in range(1,m+1):
			for j in range(1,n+1):
				
				if (self.x[i-1]==self.y[j-1]):
					self.c[i][j]=self.c[i-1][j-1]+1
					self.b[i][j]="\\"
									
				elif self.c[i-1][j]>=self.c[i][j-1]:
					self.c[i][j]=self.c[i-1][j]
					self.b[i][j]="|"
				
				else:
					self.c[i][j]=self.c[i][j-1]
					self.b[i][j]="-"
					
		
	def print_lcs(self,i,j):
		
		if (self.b[i][j]==""):
			return
		
		if (self.b[i][j]=="\\"):
			self.print_lcs(i-1,j-1)
			print(self.x[i-1],end='')
			
		elif (self.b[i][j]=="-"):
			self.print_lcs(i,j-1)
		elif (self.b[i][j]=="|"):
			self.print_lcs(i-1,j)
				 		
		
		

def run():
	
	print("Enter X")
	x=input()
	print("Enter Y")
	y=input()
	
	obj=lcs(x,y)
	obj.lcs_compute()
	print("Longest Common Subsequence-->",end='')
	obj.print_lcs(len(x),len(y))
	print()
	
	


run()

	
	
			
