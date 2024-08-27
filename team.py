#팀 결정
from random import shuffle

def team(teams: int, *members: str):
    
    team_result = {f"team_{team + 1}": [] for team in range(teams)}

    members = list(members)
    shuffle(members)

    for i, member in enumerate(members):
        team_togo = i % teams
        team_result[f"team_{team_togo + 1}"].append(member)

    for team_name, members in team_result.items():
        print(f"{team_name}: {members}")

team(3, "나", "가", "다", "라")