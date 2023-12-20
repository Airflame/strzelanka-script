import sys


def compare_users(arg1, arg2):
    if len(arg2) < len(arg1):
        album_list1, album_list2 = arg2, arg1
    else:
        album_list1, album_list2 = arg1, arg2
    compatibility = 1.0
    diff = 0.0
    for key, album_name in enumerate(album_list1):
        try:
            diff += abs(key - album_list2.index(album_name))
        except ValueError:
            diff += len(album_list1) * 2
    compatibility -= diff * 1.0 / (len(album_list1) ** 2 * 2)
    return compatibility


user = ""
user_albums = {}
for element in open(sys.argv[1], "r", encoding="utf-8").readlines():
    if "-" not in element:
        user = element.strip()
    else:
        album = element.split(";")[-1].strip()
        points = int(element.split(";")[0])
        if user not in user_albums:
            user_albums[user] = []
        user_albums[user].append(album)
users = user_albums.keys()
for user1 in users:
    for user2 in users:
        print("{};{};{}".format(user1, user2, compare_users(user_albums[user1], user_albums[user2])))
print(user_albums)
