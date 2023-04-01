def rps(p1, p2):
    counters = {"scissors": "paper",
                "paper": "rock",
                "rock": "scissors"}
    
    if p1 == p2:
        return "Draw!"
    elif counters[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"