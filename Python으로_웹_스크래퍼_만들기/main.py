# return: 함수 바깥으로 값을 보냄

def tax_calc(money):
  return(money * 0.35)

def pay_tax(tax):
  print("thank you for paying", tax)

to_pay = tax_calc(15000000)
pay_tax(to_pay)

# 위의 값과 동일 pay_tax(tax_cacl(15000000))