# user_name -> 변수, placeholder => parameter
def say_hello(user_name):
  print("hello", user_name, "how are you?") # print에서는 콤마도 사용 가능

def say_bye():
  print("bye bye")

# 괄호 안 문자, 실제로 전달한 데이터 -> argument
say_hello("nico") # 괄호 안에 데이터를 받는 function
say_hello("lynn")
say_hello("lewis")
say_hello("ralph")

print("hello world")