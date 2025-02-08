import copy # 깊은 복사를 위한 임포트
 
test_case = int(input())
 
for tc_index in range(1, test_case+1):
    a,b,c,d,e,f = map(int, input().split())  # 6명의 부하 입력
    kobon_list = [a,b,c,d,e,f] # 리스트에 담기
    lost_kobon = max(kobon_list)+1 # 7번째 부하 설정
 
    while True:
        inside_kobon_list = copy.deepcopy(kobon_list)  # deepcopy를 해서 리스트를 복사
        inside_kobon_list.append(lost_kobon) # 7번째 맴버를 추가
 
        if sum(inside_kobon_list) % 7 == 0: # 6명보다 키가 크고, 나눴을 때 정수가 나온다면,
            print(lost_kobon) # 가장 먼저 입력되는 사람이 가장 최솟값일테니...
            break
        else:
            lost_kobon +=1 # 아닐 시 1추가하고 반복 지속