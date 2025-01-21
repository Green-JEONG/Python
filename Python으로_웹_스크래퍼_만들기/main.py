# 함수: 한번 작성해서 몇번이고 재사용 가능한 코드
# parameter: 함수 안으로 데이터를 보내서 함수의 결과를 바꾸는 것, 함수 외부로부터 받게 되는 데이터
# Python은 공백에 민감

def tax_calculator(money):
  print(money * 0.35)

tax_calculator(15000000000000)
tax_calculator(150)