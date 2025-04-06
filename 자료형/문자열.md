문자열은 어떻게 만들고 사용할까?

1. 큰따옴표로 양쪽 둘러싸기 
"Hello World"

2. 작은 따옴표로 양쪽 둘러싸기
'Hello World'

3. 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
"""Life is too short, You need python"""

4. 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기 
'''Life is too short, You need python''' 

문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때

 1. 문자열에 작은따옴표 포함하기 

"Python's favorite food is perl"

'Python's favorite food is perl' -> 오류 발생 


 2. 문자열에 큰따옴표 포함하기

'"Python is very easy." he says' 

 3. 역슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함하기

'Python\'s favorite food is perl' # "Python's favorite food is perl"
"\"Python is very easy.\" he says." # '"Python is very easy." he says.'

여러 줄인 문자열을 변수에 대입하고 싶을 때 

1. 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기

multiline = "Life is too short\nYou need python"

print(multiline) 

# 출력값
# Life is too short
# You need python

2. 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기 

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

이스케이프 코드란? - 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 '문자 조합'
 \n, \t, \\, \', \" - 활용 빈도가 높은 이스케이프 코드

문자열 연산하기 

1. 문자열 더해서 연결하기

head = "Python"
tail = " is fun!"
print(head + tail) # Python is fun!

2. 문자열 곱하기

a = "python"
print(a * 2) # pythonpython

3. 문자열 곱하기를 응용하기 

print("=" * 50)
print("My Program")
print("=" * 50)

# ============================================================ 
# My Program 
# ============================================================ 

4. 문자열 길이 구하기 

a = "Life is too short"
len(a) # 17, len -> length의 약자

5. 문자열 인덱싱

a = "Life is too short, You need Python"
a[3] # e 출력 

6. 문자열 인덱싱 활용하기 

a = "Life is too short, You need Python"
a[0] # L , a[-0]과 같음 
a[12] # s
a [-1] # n
a [2] # o
a [-5] # y

7. 문자열 슬라이싱 

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b) # Life 

a = "Life is too short, You need Python"
a[0:4] # Life
a[0:3] # Lif 

# a[시작_번호:끝_번호] - 끝 번호에 해당하는 문자는 포함하지 않는다. 
# [0:3] 0<= a <3 

8.문자열을 슬라이싱하는 방법

a = "Life is too short, You need Python"
a[0:5] # Life  
a[0:2] # Li
a[5:7] # is
a[12:17] # short
a[19:0] # Li
a[:17] # Life is too short
a[:] # Life is too short, You need Python
a[19:-7] # You need 

9.슬라이싱으로 문자열 나누기 

a = "20230331Rainy"
date = a[:8]  # 20230331
weather = a[8:] # Rainy

a = "20230331Rainy" 
year = a[:4]  # 2023
day = a[4:8]  # 0331
weather = a[8:] # Rainy

# Pition 문자열을 Python으로 바꾸려면 
a = "Pition"
a[1] # i
a[1] = 'y' - 오류 발생

a = "Pitoin"
a[:1] # P
a[2:] # tion
a[:1] + 'y' + a[2:] # Python

문자열 포매팅이란?

문자열 안의 특정한 값을 바꿔야 할 경우가 있을 때 이것을 가능하게 해주는 것

문자열 포매팅 따라하기 

1. 숫자 바로 대입 
"I eat %d apples." % 3
 # I eat 3 apples.

2. 문자열 바로 대입
"I eat %s apples." % "five" 
# I eat five apples. 

3. 숫자값을 나타내는 변수로 대입. 
number = 3
I eat %d apples. % number
# I eat 3 apples. 

4. 2개 이상의 값을 넣기 

number = 10 
day = "three"
"I ate %d apples. so I was sick for %s days." %(number, day)
# I ate 10 apples. so I was sick for three days.

문자열 포맷 코드

 %s 포맷 코드는 어떤 형태의 값이든 변환해 넣을 수 있다. 

"I have $s apples" % 3
# I have 3 apples
"rate is %s" % 3.234
# rate is 3.234

포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다.

"Error is %d%." % 98 - 에러 발생

"Error is %d%%." % 98

포맷 코드와 숫자 함께 사용하기 

1. 정렬과 공백

"%10s" % "hi"
'        hi'

"%-10sjane." % 'hi'
'hi        jane'

2. 소수점 표현하기 
"0.4f" % 3.42134234 
# 3.4213

format 함수를 사용한 포매팅

1. 숫자 바로 대입하기

"I eat {0} apples.".format(3)
# I eat 3 apples. 

2. 문자열 바로 대입하기

"I eat {0} apples.format("five")
# I eat five apples

3. 숫자 값을 가진 변수로 대입하기

number = 3
"I eat {0} apples.format(number)
# I eat 3 apples

4. 2개 이상의 값 넣기

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
# I ate 10 apples. so I was sick for three days.

5. 이름으로 넣기

"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
# I ate 10 apples. so I was sick for 3 days. 

6. 인덱스와 이름을 혼용해서 넣기

"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
# I ate 10 apples, so I was sick for 3 days.

7. 왼쪽 정렬

{0:<10}.format("hi")
'hi       '

8. 오른쪽 정렬
{0:>10}.format("hi")
'       hi'

9. 가운데 정렬 
{0:^10}.format("hi")
'   hi    '

10. 공백 채우기
{0:=^10}.format("hi")

11. 소수점 표현하기
y = 3.42134234
{0:0.4f}.format(y)
# 3.4213

12. {또는} 문자 표현하기
{{ and }}.format()
{ and }

f 문자열 포매팅 

name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
# f '나의 이름은 홍길동입니다. 나이는 30입니다.'

age = 30
f'나는 내년이면 {age + 1}살이 된다.'
# f'나는 내년이면 31살이 된다.'

f 문자열 포매팅에서 딕셔너리의 사용

d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]입니다.}'
# 나의 이름은 홍길동입니다. 나이는 30입니다.

f 문자열 포매팅에서 정렬

f'{"hi":<10}' # 'hi       '
f'{"hi":>10}' # '       hi'
f'{"hi":^10}' # '   hi    '

공백 채우기

f'{"hi":=^10}' <- 가운데 정렬하고 '='로 공백 채우기
# '====hi===='
f'{"hi":!<10}' <- 왼쪽 정렬하고 '!'로 공백 채우기 
# 'hi!!!!!!!!'

소수점
y = 3.42134234
f'{y:0.4f}'
#'3.4213'
f'{y:10.4f}'
'    3.4213'

문자열 관련 함수들

1. 문자 개수 세기 - count

a = "hobby"
a.count(b) # 2

2. 위치 알려주기 1 - find

a = "Python is the best choice"
a.find('b')
# 14 - 문자열에서 b가 처음 나온 위치
a.find('k')
# -1 문자나 문자열이 존재하지 않을 때 -1 반환 

3. 위치 알려주기 2 - index

a = "Life is too short"
a.index('t')
# 8
a.index('k') # 오류 발생 / find와 차이점

4. 문자열 삽입 - join

","join('abcd')
# a,b,c,d

5. 소문자를 대문자로 바꾸기 - upper

a = "hi"
a.upper() # HI

6. 대문자를 소문자로 바꾸기 - lower

a = "HI"
a.lower() # hi

7. 왼쪽 공백 지우기 - lstrip

a = " hi "
a.lstrip()
'hi ' 

8. 오른쪽 공백 지우기 - rstrip

a = " hi "
a.rstrip()
' hi'

9. 양쪽 공백 지우기 - strip

a = " hi "
a.strip()
'hi'

10. 문자열 바꾸기 - replace

a = "Life is too short"
a.replace("Life", "Your leg")
# Your leg is too short

11. 문자열 나누기 - split

a = "Life is too short"
a.split()
['Life', 'is', 'too', 'short']
b = "a:b:c:d"
b.split(':')
['a', 'b', 'c', 'd']