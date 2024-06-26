# 변수에 값을 담는 개념을 파이썬에서는 패킹이라고하는데
# 변수에 들어간 가 있는 값을 다시 변수에 지정하는 것을
# 언패킹이라고 한다.

number = (1,2,3,4,5,6,7,8,9,10)

(one, two ,three, *others) = number
print(one)
# 이렇게 하면 number 라는 변수에 지정되어잇는 변수가
# 언패킹한 리스트에 순서대로 들어가게 되는데
# 마지막에*other는 이외의 나머지 값들을 한번에 넣는다

# 이렇게 언패킹해서 값을 넣으면 튜플로 들어가지만,
# *other로 넣은 값들은 리스트에 들어가기 때문에 주의 필요