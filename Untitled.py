#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#------------Assignment N0 # 1 --------------


# In[ ]:


Poem="Twinkle, twinkle, little star, \n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!"
print (Poem)


# In[ ]:


import sys
print("Python version which I using is :")
print (sys.version)


# In[ ]:


import datetime
calender = datetime.datetime.now()
print ("Current Date and Time : ")
print (now.strftime("%m-%d-%y %H:%M"))


# In[ ]:



radius = float(input(' Please Enter the radius of a circle: '))
area = 3.14* radius * radius

print("Area of circle \t " + str(area) )


# In[ ]:


f_name = input("Enter your First Name : ")
l_name = input("Enter your Last Name : ")
print ("reversing this be like \t" + l_name + " " + f_name)


# In[ ]:


Fname=input("Enter your First Name")
Lname =input("enter your last Name")
print (Fname + " " + Lname)
list_words= list(reversed(Fname + " "  + Lname ))
print("")
print("".join(list_words))


# In[ ]:


s1=input("enter your id")
s2=input("enter your name")

print ( s1 + "\t " + s2 )


# In[ ]:


#------------Assignment N0 # 2--------------


# In[ ]:


num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[ ]:


def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))


# In[ ]:


def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))


# In[4]:


n = len([10, 20, 30]) 
print("The length of list is: ", n) 


# In[3]:


print("Enter 'x' for exit.");
print("Enter marks obtained in 5 subjects: ");
mark1 = input();
if mark1 == 'x':
    exit();
else:
    mark1 = int(mark1);
    mark2 = int(input());
    mark3 = int(input());
    mark4 = int(input());
    mark5 = int(input());
    sum = mark1 + mark2 + mark3 + mark4 + mark5;
    average = sum/5;
    if(average>=91 and average<=100):
    	print("Your Grade is A+");
    elif(average>=81 and average<=90):
    	print("Your Grade is A");
    elif(average>=71 and average<=80):
    	print("Your Grade is B+");
    elif(average>=61 and average<=70):
    	print("Your Grade is B");
    elif(average>=51 and average<=60):
    	print("Your Grade is C+");
    elif(average>=41 and average<=50):
    	print("Your Grade is C");
    elif(average>=0 and average<=40):
    	print("Your Grade is F");
    else:
    	print("Strange Grade..!!");


# In[ ]:




