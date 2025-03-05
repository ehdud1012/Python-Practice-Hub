# -*- coding:utf-8 -*-

# 한글은 조합형

# 자음/모음 분리
#   설치 - pip install jamo
from jamo.jamo import h2j, j2hcj

a = "귤"
print(a.find("ㄱ"))  # 없다고 뜸 (-1)

b = h2j(a)          # VSCode에서 정상 출력이 안됨 / 조합형 상태로 나눠줌
b = j2hcj(b)        # 조합형 -> 자음모음 분리 
print(b)

# 자음/모음 합치기
#   github사용
#   - https://github.com/kaniblu/hangul-utils 에서 다운
#   - hangul-utils-master\hangul_utils.py파일만 가져오기

from unicode import join_jamos
c = "ㅊㅔㄹㅣ"
d = join_jamos(c)
print(d)