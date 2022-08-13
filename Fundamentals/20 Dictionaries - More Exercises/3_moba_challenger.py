# You are a pro MOBA player, you are struggling to become а master of the Challenger tier.
# So, you carefully watch the statistics in the tier.
# You will receive several input lines in one of the following formats:
# "{player} -> {position} -> {skill}"
# "{player} vs {player}"
# The "player" and "position" are strings, and the given "skill" will be an integer number.
# You need to keep track of every player.
# When you receive a player with his position and skill, add him to the players' pool, if he isn`t present, else
# add his position and skill or update his skill, only if the current position skill is lower than the new value.
# If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
# •	If they got at least one position in common, the player with
# better total skill points wins and the other is demoted from the tier -> remove him.
# •	If they have same total skill points at the same positions, the duel is tie and they both continue in the Season.
# •	If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
# You should end your program when you receive the command "Season end".
# At that point you should print the players, ordered by total skill in descending order,
# then ordered by player name in ascending order. For each player print their position and skill,
# ordered descending by skill, then ordered by position name in ascending order.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	Player and position will always be one word string, containing no whitespaces.
# •	Skill will be an integer in the range [0, 1000].
# •	There will be no invalid input lines.
# •	The program ends when you receive the command "Season end".
# Output
# •	The output format for each player is:
# "{player}: {total_skills} skill"
# - {position1} <::> {skill}
# - {position2} <::> {skill}
# …
# - {positionN} <::> {skill}"
def vs(command, pool):
    player_1, player_2 = command.split(" vs ")
    if player_1 in pool and player_2 in pool:
        for player_1_position in pool[player_1].keys():
            if player_1_position in pool[player_2].keys():
                player_1_points = sum(pool[player_1].values())
                player_2_points = sum(pool[player_2].values())
                if player_1_points < player_2_points:
                    pool.pop(player_1)
                elif player_2_points < player_1_points:
                    pool.pop(player_2)
                return pool


pool = {}
name_points = {}

while True:
    command = input()
    if command == 'Season end':
        break
    if "vs" in command:
        vs(command, pool)
    data = command.split(' -> ')
    if len(data) == 3:
        name = data[0]
        competition = data[1]
        points = int(data[2])
        if name not in pool:
            pool[name] = {}
        if competition not in pool[name]:
            pool[name][competition] = points
        else:
            if pool[name][competition] < points:
                pool[name][competition] = points

for name, stats in pool.items():
    for competition, points in stats.items():
        if name not in name_points:
            name_points[name] = points
        else:
            name_points[name] += points

for namee, max_points in sorted(name_points.items(), key=lambda x: (-x[1], x[0])):
    print(f"{namee}: {max_points} skill")
    for name, comp_points in pool.items():
        for comp, points in sorted(comp_points.items(), key=lambda x: (-x[1], x[0])):
            if name == namee:
                print(f"- {comp} <::> {points}")
