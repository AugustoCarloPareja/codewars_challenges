def is_valid_walk(walk):
    status = True
    dir = {"north": walk.count("n"),
           "south": walk.count("s"),
           "east": walk.count("e"),
           "west": walk.count("w")}
    
    if len(walk) != 10 or (dir["north"] != dir["south"]) or (dir["east"] != dir["west"]):
        status = False
    return status

if __name__ == '__main__':
    walk_array = [['n','s','n','s','n','s','n','s','n','s'],
                  ['w','e','w','e','w','e','w','e','w','e','w','e'],
                  ['w']]
    
    for walk in walk_array:
        print(f"Is valid the following walk?: {walk} \nResult: {is_valid_walk(walk)}")