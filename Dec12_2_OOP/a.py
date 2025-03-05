# -*- coding:utf-8 -*-

# PL import
#   Java 스타일     : 선택사항
#   Python 스타일   : 소스가 들어오는 형태
#       서로 임포트를 걸게 될 경우 무한루프 발생
#  

class Dog:
    pass

# 무한루프 방지로 걸어주는게 좋음 / import를 굳이 맨 위에서 할 필요가 없으니
if __name__ == "__main__":  
    from b import Cat
    c = Cat()