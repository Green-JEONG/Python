# parameter에 기본값 주기
def say_hello(user_name="anonymous"):
  print("hello", user_name)

say_hello("green")
# say_hello() # 에러
say_hello()