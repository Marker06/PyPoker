import random
import json
from sys import exit

dealt_cards = {"table":{
                "community_cards":[],
                "pot":0,
                },
                "players":{

                }
                            }


player_template = { 
                    "player_name":"",
                    "hand":[],
                    "hand_type":"",
                    "chip_pile":0,
                    "chips_out":0,
                    "total_bet":0
                                }


def addPlayer():
    global dealt_cards
    global player_template


    amount_of_players = int(3)#input("How Many Players?: "))

    for player_num in range(0,amount_of_players):

        player_name = "test_name"#input("Enter Your Name: ")

        dealt_cards["players"][player_num] = {}
        
        dealt_cards["players"][player_num].update(player_template)

        dealt_cards["players"][player_num]["player_name"] = player_name


def importDeck():
    with open("deck.json", "r") as json_deck:

        deck = json.load(json_deck)
        return deck

def shuffleDeck(deck):
    deck_shuffled = {}
    
    for suits in deck:
        deck_shuffled.update(deck[suits])

    deck_shuffled = list(deck_shuffled)

    random.shuffle(deck_shuffled)

    return deck_shuffled

def dealer(amount,location):
    global dealt_cards
    global deck_shuffled

    if type(amount) != type(0) or type(location) != type(""):
        print(type(amount), type(location))
        print("ERROR!")
        print("Invalid Types!")
        exit()

    if location != "community_cards":
        hand_type = "players"
    else:
        hand_type = "table"
    
    hand = []

    for i in range(amount):
        hand.append(deck_shuffled.pop(0))

    return hand
        



def dealCards(deal_state):
    
    global dealt_cards


    if deal_state == "preflop":
        for player_num in range(len(dealt_cards["players"])):
            dealt_cards["players"][player_num]["hand"] = dealer(2,"players")
    elif deal_state == "flop":
        dealer(3,"community_cards")
    elif deal_state in ("turn","river"):
        dealer(1,"community_cards")
    


if __name__ == "__main__":

    addPlayer()

    deck = importDeck()
    
    deck_shuffled = shuffleDeck(deck)

    

    
    

    dealCards("preflop")
    for i in dealt_cards["players"]:
        print(dealt_cards["players"][i]["hand"])
        for j in dealt_cards["players"][i]["hand"]:    
            print(deck_shuffled.count(j))
