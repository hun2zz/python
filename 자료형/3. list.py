
my_list = ['오예스', '초코파이', 123, '초코파이', '몽쉘']


# 리스트는 문자열, 숫자형 타입을 구분하지 않는다.
# 같은 값을 허용 시킴.
print(my_list)


# 자바와 똑같이 0번 인덱스부터 시작함.

print(my_list[3])

# 문자열과 똑같이 slice가 가능함

# 0번 인덱스부터 2개를 선택해서 출력함.
print(my_list[0:2])

# 안에 결과값이 있는지 확인하려면 in을 사용함.
print('몽쉘'in my_list)

# 값이 몇개가 있는지 확인하고 싶다면 len 사용
print(len(my_list))

# 값을 축하려면
my_list.append('빅파잉')
print(my_list)