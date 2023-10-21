from icons import logo, vs
from game_data import data
from random import choice


def compare(first, second):
    if first > second:
        return "A"
    elif second > first:
        return "B"


def participiant_info(data_item):
    print(
        f"{data_item['name']}, a {data_item['description']}, from {data_item['country']}"
    )
    return data_item["follower_count"]


def game():
    should_continue = True
    score = 0
    second = choice(data)
    while should_continue:
        first = second
        print(logo)
        second = choice(data)
        f_followers = 0
        s_followers = 0
        print(f"Compare A:", end=" ")
        f_followers = participiant_info(first)
        print(vs)
        print(f"Against B:", end=" ")
        s_followers = participiant_info(second)
        answer = compare(f_followers, s_followers)
        your_option = input("Who has more followers? Type 'A' or 'B': ").lower()
        if answer == your_option:
            score += 1
            print(f"You're right. Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return


game()
