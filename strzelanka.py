import sys
user = ""
albums_points = {}
albums_individual_votes = {}
for element in open(sys.argv[1], "r", encoding="utf-8").readlines():
    if "-" not in element:
        user = element.strip()
    else:
        album = element.split(".")[-1].strip()
        points = int(element.split(".")[0])
        if album in albums_points:
            albums_points[album] += points
        else:
            albums_points[album] = points
            albums_individual_votes[album] = {}
        albums_individual_votes[album][user] = points
template = "%place%. %points% pkt - **%album%** _(%users%)_"
albums_list = sorted(albums_points.items(), key=lambda item: item[1])
for index, album in enumerate(albums_list):
    entry = template.replace("%place%", str(len(albums_points) - index)).replace("%points%", str(album[1])).replace("%album%", album[0])
    users_list = []
    for user, points in sorted(albums_individual_votes[album[0]].items(), key=lambda item: item[1], reverse=True):
        users_list.append(user + " - " + str(points))
    entry = entry.replace("%users%", ", ".join(users_list))
    print(entry)