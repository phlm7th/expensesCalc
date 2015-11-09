# -*- coding: utf-8 -*-

# update 할 것들
# 1. 아까운 후보들 목록 & 목표금액과의 차이 보여주기
#   몇 백원 차이인 아까운 후보들을 보여줘봤자 그런 영수증을 구할 수가 없음.
#   천원 단위로 차이나는 것들만 보여주는 게 유용할 듯
# 1-1. 조합을 발견하지 못한 경우, 특정 금액의 영수증을 구하라고 제안 가능할 듯.
#

''' 변수 리스트
goal_money : 목표 값. 입력 받아야 함
receipt_list_input : 영수증 금액들. 입력 받아야 함
'''

from itertools import chain, combinations

# 영수증 금액을 입력 받아 int형 list로 변환해서 저장
goal_money = int(input('원하시는 금액을 입력해주세요 : '))
receipt_list_input = input('영수증 금액들을 입력해주세요. 각 영수증은 스페이스로 구분해주세요\n: ')
receipt_list = list(map(int, receipt_list_input.split()))

# 입력 받은 list로 만들 수 있는 모든 조합(단, 2개 이상의 원소를 가진)을 return 해주는 함수
def all_subsets(anylist):
    return chain(*map(lambda x: combinations(anylist, x), range(2, len(anylist)+1)))

# 영수증 리스트를 all_subsets 함수에 적용시켜서 모든 조합을 만들고 comb_list로 저장
comb_list = []
for subset in all_subsets(receipt_list):
    comb_list.append(subset)

# comb_list의 각 항목을 합한 후 그 중에서 goal_money와 같은 값을 가지는 것들만 sum_list에 저장
# goal_money와 같지 않은 것들은 sub_list에 저장
sum_list=[]
sub_list=[]
for i in range(len(comb_list)):
    if sum(comb_list[i]) == goal_money:
        sum_list.append(comb_list[i])
    else:
        sub_list.append(comb_list[i])

# 조합이 발견된 경우, 가장 영수증 개수가 적은 조합만 출력함
if len(sum_list) > 0:
    print('조합 발견!')
    print('총 발견된 조합의 수는 %d개 입니다.' % len(sum_list))
    print('그 중 가장 영수증 개수가 적은 조합은')
    print(str(sum_list[0]) + ' 입니다. (총 %d장)' % len(sum_list[0]))
# 조합이 발견되지 않은 경우, 일부 후보 조합들을 출력함
else:
    print('조합을 발견하지 못했습니다. 영수증을 구걸하러 다니세요.')
    if len(sub_list) > 9:
        for i in range(9):
            sum_sub_list = sum(sub_list[i])
            print("합 : {0:<7} / {1}".format(sum_sub_list,sub_list[i]))
    else:
        for i in range(len(sub_list)):
            sum_sub_list = sum(sub_list[i])
            print("합 : {0:<7} / {1}".format(sum_sub_list,sub_list[i]))