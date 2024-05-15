print(True)


envelope1 = 100000
envelope2 = 200000
envelope3 = 300000

print(envelope1);

# 변수 이름 규칙
"""1. 문자 또는 _로 시작 
 2, 문자, 숫자 , _로 구성
 3. 공백  x, 특수문자 x  """

# 파이썬의 주석은 한줄은 # 여러줄은 """ 로 구분함.

print(5 < 3 or 3 < 5) # true 반환 파이썬에는 || && 가 아니라 and ,or 로 작성.

print('f' in 'cat') # f라는 글자가 cat이라는 글자안에 있는지 확인 할 수 있음


lang = 'PYTHON'

print(lang[-1])
# 파이썬에서는 마지막 인덱스를 -1로 표현하여 출력이 가능하다.
print(lang[1:6])
# 1이상 6미만으로 인식을 할 수 있다. 
print(lang[1:])
# 이렇게 생략하면 마지막까지 자동으로 해줌.


print(len(lang))
# 파이썬서는 length가 len(변수)를 대입시켜서 알 수 있음.