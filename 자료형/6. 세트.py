# 세트 선언법은 세트 = {값1, 값2, ... }


a = {'제육', '보쌈', '초밥'}
b = {'짬뽕', '제육', '돈까스'}

# 위처럼 2개의 세트가 선언이 됐다면,
# 공통된 점을 교집합으로 출력할 수 있다.
# intersection
print(a.intersection(b))


# 합집함
# 중복된 값만 제거한다.
print(a.union(b))


# 차집합
# a세트에서 b 세트의 값들을 뺌 + 중복 제거하ㅁ
print(a.difference(b))