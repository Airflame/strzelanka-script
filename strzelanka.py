import sys
elements = open(sys.argv[1], "r", encoding="utf-8").readlines()
user = ""
albums = {}
albums_individual_votes = {}
for element in elements:
    if "-" not in element:
        user = element.strip()
    else:
        album = element.split(".")[-1].strip()
        points = int(element.split(".")[0])
        if album in albums:
            albums[album] += points
        else:
            albums[album] = points
            albums_individual_votes[album] = {}
        albums_individual_votes[album][user] = points
template = "%place%. %points% pkt - **%album%** _(%users%)_"
albums_list = sorted(albums.items(), key=lambda item: item[1])
length = len(albums)
for index, album in enumerate(albums_list):
    entry = template.replace("%place%", str(length - index)).replace("%points%", str(album[1])).replace("%album%", album[0])
    users_list = []
    for user, points in albums_individual_votes[album[0]].items():
        users_list.append(user + " - " + str(points))
    entry = entry.replace("%users%", ", ".join(users_list))
    print(entry)
