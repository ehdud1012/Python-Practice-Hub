# -*- coding:utf-8 -*-

# 한국어 -PL로 번역(coding)-> .java
# .java -기계어로 번역(compile)-> .class  # 여기서 번역이 안되서 에러
# .class -압축(archive)-> .jar
# .jar -실행->

# error 
#   - java 문법에 안맞게 써서 기계어로 번역 불가능한 상태
#   - 최종 산출물 안나옴 => 개발자 잘못 (내면 안됨)
# warning
#   - 지저분한, 정리안된 소스 (필요없는거 생성, 정리 안한거)
#   - 최종 산출물 잘 나옴, 실행 문제 없음 => 정리하는게 좋음
# exception
#   - 정상적인 프로그램이지만 실행할 때 외부적 요인으로 정상 실행 안되는 상태
#   - 개발자 잘못은 아님 => 해결(대비)은 해야함

# exception 해결
#   Java : 예외처리 필수, 안하면 error
#       try-catch-finally - 직접처리
#           1) 신입사원 주제에 해결?
#           2) 대응 방법까지 내장 -> 다른 프로젝트에서 사용하기가 .. (재사용 ↓)
#       throws - 미루기
#       

#   Python : 예외처리 안해도 됨 (회사 가서는 해야하니까 신경 쓰기)
#       - interpreter 방식 : 한국어 -PL로 번역(coding)-> .py -> 실행
#       - 일단 실행은 됨 -> 실행도중 뭔가 문제  => error도 아니고 exception도
#           a = 10
#           print(a)
#           asdasd 경계가 애매함
#       - try-catch 비슷한 것만 존재
#       - 자바는 .jar을 주고 받기 때문에 수정 불가
#         파이썬은 .py를 주고 받아서 수정 가능 
#           => 1),2) 문제가 아님 -> throws 무의미
#       - try - except - else - finally

# 예제
x = int(input("x : "))
y = int(input("y : "))

# 세세하게 경우 나누는 버전
# try:
#     z = x / y
#     print(z)

#     l = [23, 445]
#     print(l[y])
# except ZeroDivisionError:
#     print("나누기 0?")
# except IndexError:
#     print("리스트에 없음")
# --------------------------------------
# 하나로 정리
# try:
#     z = x / y
#     print(z)

#     l = [23, 445]
#     print(l[y])
# except:
#     print("아무튼 문제 있음")
# print("문제 있든 말든 실행")

# --------------------------------------
def divide(x, y):
    try:
        z = x / y
        return z
    except Exception as e:
        print(e) # 오류 메세지 나옴
        return -99
    else:
        print("문제 없음(리턴보다 먼저는 아니라서 return이 있을 때는 안통함)")
    finally:
        print("문제 있던 말던 리턴보다 먼저 실행")
        
    print("a") # 위에서 리턴되니까 실행 X

print(divide(x, y))

try:
    a = 10
    # b = asdas
except Exception as e:
    print(e)
else:
    print("문제 없음(리턴보다 먼저는 아니라서 return이 있을 때는 안통함)")