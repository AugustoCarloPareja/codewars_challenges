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

if __name__ == '__main__':
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    
    matches = [
        (scissors, rock),
        (rock, paper),
        (paper, scissors),
        (scissors, rock),
        (paper, rock),
        (paper, rock)
        ]
    
    for idx, match in enumerate(matches):
        print(f"""
        [ MATCH {idx+1} ]
        Player 1: {match[0]}
        Player 2: {match[1]}
        Result: {rps(*match)}
        """)