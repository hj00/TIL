
# coding: utf-8

# 문제 4-1)아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요. 참고로 print('*', end='')와 같이 print 함수를 사용하면 줄바꿈 없이 화면에 출력할 수 있습니다.

# In[2]:


for i in range(5):
    print('*', end='')


# 문제 4-2) 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해보세요. (힌트: 이중 루프 사용)

# In[6]:


for i in range(4):
    for j in range(5):
        print('*', end='')
    print('\n')


# In[7]:


for i in range(4):
    for j in range(5):
        print('*', end='')
    print('')


# 문제 4-3) 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해보세요.

# In[9]:


for i in range(5):
    print("*"*(i+1))


# 문제 4-4) 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

# In[10]:


for i in range(5):
    print('*'*(5-i))


# 문제 4-5) 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

# In[15]:


for i in range(5):
    print(" "*(4-i)+'*'*(i+1))


# 문제 4-6) 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

# In[17]:


for i in range(5):
    print(" "*i+'*'*(5-i))


# 문제 4-7) 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

# In[20]:


for i in range(5):
    print(' '*(4-i)+'*'*(2*i+1)+' '*(4-i))


# 문제 4-8) 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성 해보세요.

# In[22]:


for i in range(5):
    print(' '*i + '*'*(9-2*i) + ' '*i)


# 문제 4-9) 이중 루프를 이용해 신문 배달을 하는 프로그램을 작성하세요. 단, 아래에서 arrears 리스트는 신문 구독료가 미납된 세대에 대한 정보를 포함하고 있는데, 해당 세대에는 신문을 배달하지 않아야 합니다.

# In[23]:


apart = [[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]


# In[28]:


for i in apart:
    for j in i:
        if j not in arrears:
            print("Delevery: ", j)


# 문제 5-1) 두 개의 정수 값을 받아 두 값의 평균을 구하는 함수를 작성하세요.

# In[33]:


import numpy as np


# In[40]:


def myaverage(a, b):
    mean = (a+b)/2
    return mean


# In[41]:


myaverage(10, 15)


# 문제 5-2) 함수의 인자로 리스트를 받은 후 리스트 내에 있는 모든 정수 값에 대한 최댓값과 최솟값을 반환하는 함수를 작성하세요.

# In[44]:


def get_max_min(data_list):
    up = max(data_list)
    down = min(data_list)
    return (print("min: ", down), print("max: ", up))


# In[45]:


a = [44, 489, 53, 55, 10, 77]
get_max_min(a)


# 문제 5-3) 절대 경로를 입력받은 후 해당 경로에 있는 *.txt 파일의 목록을 파이썬 리스트로 반환하는 함수를 작성하세요.

# In[46]:


import os


# In[48]:


wd = os.getcwd()
os.listdir(wd)


# In[49]:


def get_txt_list(path):
    os_list = os.listdir(path)
    txt_list = []
    for l in os_list:
        if l.endswith('txt'):
            txt_list.append(l)
    return txt_list


# In[50]:


get_txt_list('c:/')


# 문제 5-4) 체질량 지수(Body Mass Index, BMI)는 인간의 비만도를 나타내는 지수로서 체중과 키의 관계로 아래의 수식을 통해 계산됩니다. 여기서 중요한 점은 체중의 단위는 킬로그램(kg)이고 신장의 단위는 미터(m)라는 점입니다.
# 
# BMI=체중(kg)신장(m)2
# 일반적으로 BMI 값에 따라 다음과 같이 체형을 분류하고 있습니다.
# 
# BMI <18.5, 마른체형
# 18.5 <= BMI < 25.0, 표준
# 25.0 <= BMI < 30.0, 비만
# BMI >= 30.0, 고도 비만
# 함수의 인자로 체중(kg)과 신장(cm)을 받은 후 BMI 값에 따라 '마른체형', '표준', '비만', '고도 비만' 중 하나를 출력하는 함수를 작성하세요.

# In[1]:


def get_bmi(weight, height):
    height = height * 0.01
    BMI = weight/((height*height))
    result = ''
    if BMI < 18.5:
        result = '마른체형'
    elif BMI>=18.5 and BMI<25.0:
        result = '표준'
    elif BMI>=25.0 and BMI<30.0:
        result = '비만'
    else:
        result = '고도 비만'
    return result    


# In[2]:


get_bmi(50, 163)


# 문제 5-5) 사용자로부터 키(cm)와 몸무게(kg)를 입력받은 후 BMI 값과 BMI 값에 따른 체형 정보를 화면에 출력하는 프로그램을 작성해 보세요. 파이썬에서 사용자로부터의 입력은 input() 함수를 사용하며, 작성된 프로그램은 계속해서 사용자로부터 키와 몸무게를 입력받은 후 BMI 및 체형 정보를 출력해야 합니다(무한 루프 구조).

# In[3]:


def get_bmi(weight, height):
    height = height * 0.01
    BMI = weight/((height*height))
    result = ''
    print("BMI : ", BMI)
    if BMI < 18.5:
        result = '마른체형'
    elif BMI>=18.5 and BMI<25.0:
        result = '표준'
    elif BMI>=25.0 and BMI<30.0:
        result = '비만'
    else:
        result = '고도 비만'
    return result


# In[ ]:


while 1:
    height = input("Height : ")
    weight = input("Weight : ")
    get_bmi(float(weight), float(height))


# 문제 5-6) 삼각형의 밑변과 높이를 입력받은 후 삼각형의 면적을 계산하는 함수를 작성하세요.

# In[4]:


def get_triangle_area(width, height):
    tri = width*height*(1/2)
    return tri


# In[5]:


get_triangle_area(5,10)


# 문제 5-7) 함수의 인자로 시작과 끝 숫자를 받아 시작부터 끝까지의 모든 정수값의 합을 반환하는 함수를 작성하세요(시작값과 끝값을 포함).

# In[67]:


def add_start_to_end(start, end):
    s = []
    for i in range(start, end):
        s.insert(-1, i)
    s.insert(-1, end)
    return sum(s)


# In[70]:


def add_start_to_end(start, end):
    s = []
    for i in range(start, end):
        s.append(i)
    s.insert(-1, end)
    return sum(s)


# In[71]:


add_start_to_end(0, 5)


# 문제 5-8) 함수의 인자로 문자열을 포함하는 리스트가 입력될 때 각 문자열의 첫 세 글자로만 구성된 리스트를 반환하는 함수를 작성하세요. 예를 들어, 함수의 입력으로 ['Seoul', 'Daegu', 'Kwangju', 'Jeju']가 입력될 때 함수의 반환값은 ['Seo', 'Dae', 'Kwa', 'Jej']입니다.

# In[65]:


def get_three(str_list):
    new_list = []
    for i in str_list:
        new_list.append(i[:3])
    return new_list


# In[66]:


get_three(['Seoul', 'Daegu', 'Kwangju', 'Jeju'])

