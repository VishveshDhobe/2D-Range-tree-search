#!/usr/bin/env python
# coding: utf-8

# In[49]:


import matplotlib.pyplot as plt
import math


# Key fuction for sorting
def rx(p):
    return p[0]
def ry(p):
    return p[1]


# Fuction for Searching in Tree
def search(x,y,flag,l,x1,y1,x2,y2):
    
    # Flag is 0 when sorting is needed according to X coordinate of Point
    if flag==0:
        l.sort(key=rx)
        flag=1
        index=len(l)//2
        if index!=0 and len(l)%2==0:
            index-=1
            
        point1 = [l[index][0], y1]
        point2 = [l[index][0], y2]
        x_values = [point1[0], point2[0]]
        y_values = [point1[1], point2[1]]
        
        # Drawing vertical line with blue color
        plt.plot(x_values, y_values,color='b')
        
        #Return True if point found
        if l[index][0]==x and l[index][1]==y:
            return 1,True
        else:
            #Return False if point not found
            if(index==0):
                return 0,False
            else:
                #Calling recursive search fuction for specific range of points
                if(x<=l[index][0]):
                    interation,f=search(x,y,flag,l[0:index],x1,y1,l[index][0],y2)
                    return(interation+1,f)
                
                else:
                    interation,f=search(x,y,flag,l[index+1:len(l)],l[index][0],y1,x2,y2)
                    return(interation+1,f)
    
    # Flag is 1 when sorting is needed according to Y coordinate of Point
    else:
        l.sort(key=ry)
        flag=0
        index=len(l)//2
        if index!=0 and len(l)%2==0:
            index-=1
            
        point1 = [x1, l[index][1]]
        point2 = [x2, l[index][1]]
        x_values = [point1[0], point2[0]]
        y_values = [point1[1], point2[1]]
        
        # Drawing horizontal line with red color
        plt.plot(x_values, y_values,color='r')
        
        #Return True if point found
        if l[index][0]==x and l[index][1]==y:
            return 1,True
        else:
            #Return False if point not found
            if(index==0):
                return 0,False
            else:
                
                #Calling recursive search fuction for specific range of points
                if(y<=l[index][1]):
                    interation,f=search(x,y,flag,l[0:index],x1,y1,x2,l[index][1])
                    return(interation+1,f)
                
                else:
                    interation,f=search(x,y,flag,l[index+1:len(l)],x1,l[index][1],x2,y2)
                    return(interation+1,f)
  
if __name__ == "__main__":
    
    # Reading input points fron "input.txt"
    file = open("./input.txt","r")
    Number_of_points=int(file.readline())
    points=[]
    for i in range(Number_of_points):
        temp=list(map(int,file.readline().split()))
        points.append(temp)
    
    # Plotting point using sactter method
    for i in range(n):
        plt.scatter(points[i][0],points[i][1])
    plt.grid()
    plt.rcParams["figure.figsize"] = [5,5]
    x1=math.floor((min(points,key=rx))[0])-1
    x2=math.ceil((max(points,key=rx))[0])+1
    y1=math.floor((min(points,key=ry))[1])-1
    y2=math.ceil((max(points,key=ry))[1])+1
    
    print("Enter point to search:-")
    x,y=map(int,input().split())
    flag=0
    
    # Calling recursive search fuction
    interation,flag=search(x,y,flag,points,x1,y1,x2,y2)
    if flag==True:
        print("(",x,",",y,") Found in",interation,"interation")
        plt.show()
    else:
        print("(",x,",",y,") Not Found after",interation,"interation")
        plt.show()


# In[ ]:




