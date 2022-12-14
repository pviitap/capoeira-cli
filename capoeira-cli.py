import sys
import random

attacks = {
    "martelo": {"target": "head", "description" : "sidekick"}
    , "compasso": {"target": "ribs"}
    , "armada": {"target": "ribs"}
    , "bencao": {"target": "chest"}
    , "meia lua de frente": {"target": "head", "description" :"half moon kick"}
    , "queixada": {"target": "head"}
}
defences = {
    "cocorinha": {"counter": ["ribs", "head"]}
    , "negativa": {"counter": ["head"]}
    , "au": {"counter": ["legs"]}
    , "rasteira": {"counter": ["head"], "description" : "sweep"}
    , "baixa": {"counter": ["head"], "description" : "low ginga"}
    , "queda de quatro": {"counter": ["chest", "ribs"], "description" : "fall from four"}
}
movements = {
    "ginga": {"stance": "high"}
    , "role": {"stance": "low"}
    , "corta capim": {"stance": "low"}
}


class Player:
    stance = "high"
    prev_action = "ginga"
    next_action = "ginga"


def react_to(opponent_action):
    if opponent_action in attacks.keys():
        target = attacks[opponent_action]["target"]
        valid_choices = [d for d in defences if target in defences[d]["counter"]]
        response = random.choice(valid_choices)
    elif opponent_action in defences.keys():
        response = random.choice(list(movements))
    elif opponent_action in movements.keys():
        response = random.choice(list(attacks) + list(movements))
    else:
        raise Exception("Unknown action")
    return response


def update():
    print("*** " + player2.next_action + " vs " + next_action + " ***")
    if player2.next_action not in list(attacks.keys()):
        return
    target = attacks[player2.next_action]["target"]
    valid_defences = [d for d in defences if target in defences[d]["counter"]]
    if player1.next_action not in valid_defences:
        raise ValueError("Player2 won!")


player1 = Player()
player2 = Player()

while True:
    player2.next_action = react_to(player1.next_action)
    print("player2: " + player2.next_action)
    ask_input = input(">> ")
    next_action = \
        [x for x in list(attacks.keys()) + list(defences.keys()) + list(movements.keys()) if x.startswith(ask_input)][0]
    player1.next_action = next_action
    update()
