from math import *
top=-1
a=[]
v=dict()
def prec(e):
	if(e=='+' or e=='-'):
		return 1
	elif(e=='*' or e=='/'):
		return 2
	elif(e=='^'):
		return 3
	elif(e=='%'):
		return 4
	return -1
def isn(e):
	if(e>=0 and e<=9):
		return 1
	return 0
def isc(e):
	if(e>='a' and e<='z'):
		return 1
	return 0
def iss(e):
	if(e=='+' or e=='-' or e=='*' or e=='/' or e=='^' or e=='%'):
		return 1
	return 0
def isse(e):
	if(e=='(' or e==')'):
		return 1
	return 0
def itp(b):
	c=[]
	for i in range(len(b)):
		if(b[i]>='a' and b[i]<='z'):
			c.append(b[i])
		elif(b[i]=='('):
			a.append(b[i])
		elif(b[i]==')'):
			while(a[len(a)-1]!='(' and len(a)!=0):
				c.append(a.pop())
			if(a[len(a)-1]=='('):
				a.pop()
		else:
			while(len(a)!=0 and prec(b[i])<prec(a[len(a)-1])):
				c.append(a.pop())
			a.append(b[i])
	while(len(a)!=0):
		c.append(a.pop())
	return c
def eval(c):
	d=[]
	e=0
	f=0
	for i in range(len(c)):
		if(isc(c[i])):
			d.append(v[c[i]])
		elif(iss(c[i])==1):
			e=d.pop()
			f=d.pop()
			if(c[i]=='+'):
				d.append(e+f)
			elif(c[i]=='-'):
				d.append(f-e)
			elif(c[i]=='*'):
				d.append(f*e)
			elif(c[i]=='/'):
				d.append(f/e)
			elif(c[i]=='^'):
				d.append(int(pow(f,e)))
			elif(c[i]=='%'):
				d.append(f%e)	
	for j in d:
		print("Result is: ",j)
m=int(input("Press 1 for formula evaluation\n2 for quadratic equation: "))
if(m==1):
	b=str(input("Enter the formula: "))
	s=dict()
	t=[]
	for i in b:
		if(iss(i)!=1 and isse(i)!=1):
			s[i]=0
	for i in s:
		z=int(input("Enter the value of "+i+" : "))
		v[i]=z
	c=itp(b)
	eval(c)
elif(m==2):
	x=int(input("Enter the co-efficient of x^2 :"))
	y=int(input("Enter the co-efficient of x: "))
	z=int(input("Enter the constant: "))
	w=pow(y,2)-(4*x*z)
	if(w>=0):
		print("Roots are real")
		r1=(-y+sqrt(w))/(2*x)
		r2=(-y-sqrt(w))/(2*x)
		if(r1==r2):
			print("Both roots are equal and the roots are: "+str(r1)+"\t"+str(r2))
		else:
			print("Roots are: "+str(r1)+"\t"+str(r2))
	else:
		print("Roots are imaginary and the roots are: "+str(-y/(2*x))+" +i "+str(sqrt(-w)/(2*x))+"\t"+str(-y/(2*x))+" -i "+str(sqrt(-w)/(2*x)))

else:
	print("Enter a valid operation...")


