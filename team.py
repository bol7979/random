#챗GPT, 정상 작동, 이해불가

import random

# 시작 설정
team_number = 3  # 팀의 수
member_list = ["가", "나", "다", "라", "마", "바", "사"]  # 멤버의 목록
random.shuffle(member_list)  # 멤버 목록을 랜덤으로 섞기

# 팀의 생성
teams = {f'team_{i + 1}': [] for i in range(team_number)}

# 팀의 멤버 선택
team_index = 0
while member_list:  # 멤버 리스트가 비어있지 않은 동안 실행
    team_name = f'team_{team_index + 1}'
    selected_member = member_list.pop()  # 멤버 리스트에서 한 명을 꺼내옴
    teams[team_name].append(selected_member)  # 현재 팀에 멤버 추가
    team_index = (team_index + 1) % team_number  # 다음 팀으로 순환

# 결과 출력
for i in range(1, team_number + 1):
    team_name = f'team_{i}'
    print(f"팀 {i}: {teams[team_name]}")

