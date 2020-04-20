# 파이썬에서 입력을 받는 함수가 있습니다~~ 구글링해서 찾아보세요!

print('문제 1. 전화번호 받기')

print('조건 1. 저장할 때는 공백 문자 없이')
print('조건 2. -, ., , 등이 들어올 때 전부 제외 하고 숫자만 저장!')

phone_number = input("전화번호 입력")
phone_number = phone_number.replace('-','')
phone_number = phone_number.replace('.','')
phone_number = phone_number.replace(',','')
phone_number = phone_number.strip()
print(phone_number)


print('문제 2. 영어 이름 받기')
print('choi juwon 을 입력 받으면,')
print('first name : Choi, last name: Juwon 이 출력되게 만들기')


english_name = input("영어이름받기")
name = english_name.split()
first_name= name[0]
upper1=first_name[0].upper()
last_name = name[1]
upper2=last_name[0].upper()
first_name_final= upper1 + first_name[1:]
second_name_final= upper2 + last_name[1:]
print("first name :"+ first_name_final + ", last name: "+ second_name_final)