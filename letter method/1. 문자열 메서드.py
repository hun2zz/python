letter = "How are You?"


# 전부 소문자로 바꿔줌
print(letter.lower())


# 전부 대문자볼 변환해줌
print(letter.upper())

# 첫 글자만 대문자로 하고 싶으면 ?
print(letter.capitalize())


# 각 단어들을 첫 글자만 대문자로 
print(letter.title())

# 대소문자를 뒤집고 싶다면 ?
print(letter.swapcase())


# 문자열을 나눠주고 싶다면 ?
# 띄어쓰기 기준으로 리스트 형태로 반환해줌.
print(letter.split())

# 특정 글자가 몇 번 쓰였는지 확인
print(letter.count('How'))