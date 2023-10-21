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
        f"{data[index1]['name']}, a {data[index1]['description']}, from {data[index1]['country']}"
    )
    return data[index1]["follower_count"]


def checking_answer(answer, your_guess, point):
    if answer == your_guess:
        print("You win!")
        return point + 1
    else:
        print("You lose")
        return False


def game():
    should_continue = True
    score = 0
    s_index = randint(0, len(data) - 1)
    while should_continue:
        f_index = s_index
        print(logo)
        s_index = randint(0, len(data) - 1)
        f_followers = 0
        s_followers = 0
        print(f"Compare A:", end=" ")
        f_followers = participiant_info(f_index)
        print(vs)
        print(f"Against B:", end=" ")
        s_followers = participiant_info(s_index)
        print(f"first followers {f_followers} second followers {s_followers}")
        answer = compare(f_followers, s_followers)
        your_option = input("Who has more followers? Type 'A' or 'B': ")
        score = checking_answer(answer, your_option, score)
        print(f"You're right. Current score: {score}")


game()
