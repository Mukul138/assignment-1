
# coding: utf-8

# In[1]:


a=10
b=20
print (a)
print(b)
c=a
a=b
b=c
print (a)
print (b)


# In[2]:


a=int(input())
if(a%2==0):
    print("even")
else:
    print("odd")


# In[ ]:


import math
n=int(input(n))
print(math.sqrt(n))


# In[2]:


import math
a=int(input("Enter no. "))
print(" ",math.sqrt(a))


# In[4]:


n=int(input())
for i in range (1,n):
    print(i)
for i in range (n,1,-1):
    print(i)
    


# In[3]:


import math
pi=math.pi


# In[4]:


def volume(r):
    vol=(4/3)*pi*r*r*r
    return vol


# In[5]:


r=int(input())
volume(r)


# In[6]:


for i in range (1,101):
    if(i%2==0):
        print(i,"is even")
    else:
        print(i,"is odd ")


# In[7]:


n=int(input())
def sum(n):
    add=0
    for i in range(0,n):
        if (i%3==0 , i%5==0):
            add=add+i
        else:
            pass
    return add 
a=sum(n)
print(a)


# In[9]:


import math

a = int(input("Please Enter a Value of a Quadratic Equation : "))
b = int(input("Please Enter b Value of a Quadratic Equation : "))
c = int(input("Please Enter c Value of a Quadratic Equation : "))

discriminant = (b * b) - (4 * a * c)

if(discriminant > 0):
    root1 = (-b + math.sqrt(discriminant) / (2 * a))
    root2 = (-b - math.sqrt(discriminant) / (2 * a))
    print("Two Distinct Real Roots Exists: root1 = {} and root2 = {}".format(root1, root2))
elif(discriminant == 0):
    root1 = root2 = -b / (2 * a)
    print("Two Equal and Real Roots Exists: root1 = {} and root2 = {}".format(root1, root2))
elif(discriminant < 0):
    print("Root are imaginary!!!!")


# In[18]:


n=int(input("Enter no."))
a=0
while(n!=0):
    n=n//10
    a+=1
print("total no",a)


# In[35]:


n=int(input("Enter the no. "))
print("Press 1 to Add or Press 2 to mul")
a=int(input("Enter choice "))
sum=0
mul=1
if a==1:
    for i in range(1,n+1):
        sum+=i
    print(sum)
elif a==2:
    for i in range(1,n+1):
        mul*=i
    print(mul)
else:
    pass


# In[36]:


for n in range(2000,3200+1):
    if (n%7==0 , n%5!=0):
        print(n)


# In[10]:


sum=0
for i in range(1,100+1):
    a=i**2
    sum+=a
print(sum-sum**2)


# In[1]:


for i in range (1,5):
    print("*"*i)


# In[2]:


for i in range (5,0,-1):
    print(i*"*")


# In[4]:


a=int(input("Enter a number :")) #done
for i in range(0,a+1):
    print(i*str(i))


# In[5]:


n=5
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))


# In[6]:


def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
def lcm(a,b): 
    return (a*b) / gcd(a,b) 
a=int(input("Enter the no. "))
b=int(input("Enter the no. "))
  
print('LCM of', a, 'and', b, 'is', lcm(a, b))

