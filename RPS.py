#the program assumes that the opponent’s next move can be predicted from their recent moves (the last 3 moves).
#a dictionary (pattern_dict) is used to store how often a certain sequence of moves is followed by Rock (R), Paper (P), or Scissors (S).
#when predicting, the program looks at the dictionary and checks which move most frequently follows it. then selects the counter move.

def player(prev_play, opponent_history=[], pattern_dict={}):
    #set length of the sequence
    n = 3

    #save opponent's move history
    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)
    
    #if not enough to make prediction yet
    if len(opponent_history) < n:
        return "R"
    
    #create sequence from the last 3 moves of the opponent
    seq = "".join(opponent_history[-n:])

    #update the previous sequence into dictionary only if there is enough opponent history
    if len(opponent_history)>n:
        prev_seq = "".join(opponent_history[-n-1:-1]) 
        if prev_seq not in pattern_dict:
            pattern_dict[prev_seq] = {"R":0, "P":0, "S":0}
        if prev_play in ["R", "P", "S"]:
            pattern_dict[prev_seq][prev_play] += 1
    
    #predict opponent's next move
    if seq in pattern_dict:
        predicted = max(pattern_dict[seq], key=pattern_dict[seq].get)
    else:
        predicted = "R"

    #return the counter move
    return {"R":"P", "P":"S", "S":"R"}[predicted]

  