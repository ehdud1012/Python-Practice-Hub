# -*- coding:utf-8 -*-

# a priori - 비지도 학습
#   - 연관관계 : A,B가 동시에 잘 나올 확률
#   - 추천 시스템에 많이 쓰임
#   - scikit-learn에 a priori는 없음
#       단독 따로 설치 - pip install apyori

# supportData (지지도)
#   0.1로 지정 -> 100명중에 10명(10%) 이상이 산 상품을 대상으로 하자
#       - 전체 손님이 100명인데, 치킨은 80명 : 치킨은 여러명이 사서 의미 있음
#       - 전체 손님이 10명인데 , 볼펜은 1명 : 너무 적은 손님이 사서 계산할때 제외하자

# confidenceData (신뢰도)
#   0.5로 지정 -> 같이 나올 확률이 0.5(50%) 이상인 것만 보여달라
#       - 치킨을 산 사람이 맥주도 살 확률 : 0.7 - o
#       - 맥주을 산 사람이 피자도 살 확률 : 0.3 - x
#       ...
#       - 치킨/맥주를 산 사람이 피자를 살 확률 : 0.6 - o
#       ...
from apyori import apriori

trainData = [["치킨", "치킨", "피자", "맥주"],
             ["치킨", "맥주"],
             ["피자", "소주"],
             ["피자", "치킨", "맥주"]]
result = apriori(trainData, 
                    min_support=0.5,  # 4명중에 2명이상은 산걸로
                    min_confidence=0.5 # A -> B일 확률 50% 이상인것만 볼래
                )
result = list(result)
for r in result:
    for r2 in r.ordered_statistics:
        print("%s를 산 사람이 %s도 살 확률 : %f" % 
              (list(r2.items_base), 
               list(r2.items_add), 
               r2.confidence))
        print(r2.lift)

# set : 중복X, 순서?
# frozenset : 수정 안되는 set

# lift : apyori라이브러리에서만 제공해주는
#   (피자, 맥주/치킨 같이 나올 확률) / (각각 따로 나올 확률)
#   => 독립적으로 나올때보다 같이 나올 확률이 얼마나 더 크나