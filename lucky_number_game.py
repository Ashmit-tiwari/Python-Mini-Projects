"""
Problem Statement:

Two players participate in the Lucky Number Challenge.
Both players enter their names and the total number of rounds.
If the total number of rounds is odd, Player 1 wins.
If the total number of rounds is even, Player 2 wins.
The program should display the winner and a congratulatory message.
"""

print("-----THE------PICKUP-----GAME--------")
player_1 = input("Enter the player name:")
player_2 = input("Enter the player name: ")
Total_Rounds = int(input("Enter the numbers of Rounds--"))
print("--------PLAYER-1---START!!---First------- ")
if Total_Rounds % 2 == 0:
    print("player_2 Wins!!")
    print("Congrats")
else:
    print("player_1 Wins!!")
    print("Congrats")