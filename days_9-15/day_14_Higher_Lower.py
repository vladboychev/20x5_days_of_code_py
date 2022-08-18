import random
from day_14_game_data import data


# get random account
def get_account_data():
    return random.choice(data)


account1 = get_account_data()
account2 = get_account_data()
while account1["name"] == account2["name"]:
    account2 = get_account_data()
score = 0
game = True
while game:
    print(f"Compare A: {account1['name']}, {account1['description']} from {account1['country']}.")
    print()
    print(f"Against B: {account2['name']}, {account2['description']} from {account2['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    followers_A = account1["follower_count"]
    followers_B = account2["follower_count"]
    if (choice == "a" and followers_A > followers_B) or (choice == "b" and followers_B > followers_A):
        score += 1
        print(f"You're right! Current score: {score}.")
        account1 = account2
        account2 = get_account_data()
    else:
        game = False
        print(f"Sorry, You got it wrong. Current score: {score}.")
