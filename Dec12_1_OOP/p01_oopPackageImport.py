# -*- coding:utf-8 -*-

# Java
#   객체 생성
#       패키지명.클래스명 변수명 = new 패키지명.생성자();
#   import : 클래스명 쓸 때 패키지명 생략 가능 (옵션사항, 필수 X)

# Python
#   package 
#       필수 아님
#       이름 마음대로
#       __init__.py 파일이 필요 (생성만 하면 됨)
#  
#   import
#       다른 모듈에 있는거 쓰려면 필수
#       거기 있는 소스가 들어오는 느낌 (코드 전체의 이롱)

# 패키지 할랭
#   animal이라는 패키지(폴더) 생성

#------------------------------------------
# 방법 1
# import import 패키지명.모듈명
# import animal.pet
# 객체 생성 변수명 = 패키지명.모듈명.클래스명(...)
# d = animal.pet.Dog("초코", 3)
# d.showInfo()
#------------------------------------------
# 방법 2
# import 패키지명.모튤명 as 이름
# import animal.pet as ap
# 객체 생성 변수명 = 이름.클래스명(...)
# d = ap.Dog("초코", 3)
# d.showInfo()
#------------------------------------------
# 방법 3
# from 패키지명.모듈명 import 가져올거
from animal.pet import Dog
d = Dog("초코", 3)
d.showInfo()

from product.snack import Snack
s = Snack("빼뺴로", 1000)
s.showSnackInfo()

import menu
m = menu.Menu()