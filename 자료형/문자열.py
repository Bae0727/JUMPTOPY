# 문자열을 만들고 사용하는 방법

"Hello World"
'Hello World'
"""Life is too short, You need python"""
'''Life is too short, You need python''' 

# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때

# 1. 문자열에 작은따옴표 포함하기 

"Python's favorite food is perl"

"""
'Python's favorite food is perl' -> 오류 발생 
"""

# 2. 문자열에 큰따옴표 포함하기

'"Python is very easy." he says' 

# 3. 역슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함하기

'Python\'s favorite food is perl' # "Python's favorite food is perl"
"\"Python is very easy.\" he says." # '"Python is very easy." he says.'

# 여러 줄인 문자열을 변수에 대입하고 싶을 때 

# 1. 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기기

multiline = "Life is too short\nYou need python"

print(multiline) 

# 출력값
# Life is too short
# You need python

# 2. 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기 

multiline = '''
Life is too short
You need python
'''
print(multiline)

multiline = """
Life is too short
You need python
"""
print(multiline)

# Life is too short
# You need python

# 이스케이프 코드란? - 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 '문자 조합'
# \n, \t, \\, \', \" - 활용 빈도가 높은 이스케이프 코드

# 문자열 연산하기 

# 1. 문자열 더해서 연결하기

head = "Python"
tail = " is fun!"
print(head + tail) # Python is fun!

# 2. 문자열 곱하기

a = "python"
print(a * 2) # pythonpython

# 3. 문자열 곱하기를 응용하기 

print("=" * 50)
print("My Program")
print("=" * 50)

# ============================================================ 
# My Program 
# ============================================================ 


# 4. 문자열 길이 구하기 

a = "Life is too short"
len(a) # 17, len -> length의 약자

# 5. 문자열 인덱싱

a = "Life is too short, You need Python"
a[3] # e 출력 

# 6.문자열 인덱싱 활용하기 

a = "Life is too short, You need Python"
a[0] # L , a[-0]과 같음 
a[12] # s
a [-1] # n
a [2] # o
a [-5] # y

# 7. 문자열 슬라이싱 

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b) # Life 

a = "Life is too short, You need Python"
a[0:4] # Life
a[0:3] # Lif 


# a[시작_번호:끝_번호] - 끝 번호에 해당하는 문자는 포함하지 않는다. 
# [0:3] 0<= a <3 

# 8.문자열을 슬라이싱하는 방법

a = "Life is too short, You need Python"
a[0:5] # Life  
a[0:2] # Li
a[5:7] # is
a[12:17] # short
a[19:0] # Li
a[:17] # Life is too short
a[:] # Life is too short, You need Python
a[19:-7]