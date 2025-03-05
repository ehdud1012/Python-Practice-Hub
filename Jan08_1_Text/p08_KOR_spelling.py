# -*- coding:utf-8 -*-

# 오타 검사
# py-hanspell : 
#   pip X 
#   개인 개발자가 네이버 맞춤법 검사기 API로 개발 -> 개발자 github에
#   pip써서 github에 있는거 설치하려면 컴에 git있어야 -> https://git-scm.com/
#   설치 - pip install git+주소
#        - pip install git+https://github.com/ssut/py-hanspell

# 근데 지금 네이버 맞춤법 검사기 API가 안되네?
# 그냥 만들지 ..

from hanspell.spell_checker import check

sentence = "오탸눈 내갸 젱일 잟하눈거야"
result = check(sentence)
print(result)


