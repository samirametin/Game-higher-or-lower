from icons import logo, vs
from game_data import data
from random import randint


def compare(first, second):
    if first > second:
        return "A"
    elif second > first:
        return "B"


def participiant_info(index1):
    print(
        f"Compare A: {data[index1]['name']}, a {data[index1]['description']}, from {data[index1]['country']}"
    )
    return data[index1]["follower_count"]


f_index = randint(0, len(data) - 1)
s_index = randint(0, len(data) - 1)
f_followers = 0
s_followers = 0

f_followers = participiant_info(f_index)
s_followers = participiant_info(s_index)
print(f"ff-{f_followers} ss-{s_followers}")
