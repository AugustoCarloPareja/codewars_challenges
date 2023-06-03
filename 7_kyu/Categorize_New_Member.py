def open_or_senior(data):
    return ["Senior" if age>54 and handicap>7 else "Open" for age, handicap in data]

if __name__ == '__main__':
    new_members = [
        [(82, 24), (52, 6), (75, -2)],
        [(40, 12), (23, 14), (86, 21), (46, 11), (18, 9), (51, 6)],
        [(44, 14), (75, 9), (43, 21), (73, 12), (64, 9), (82, 18)],
        [(45, 15), (66, 18), (64, -2), (62, 3)]
        ]
    
    for member in new_members:
        print(f"{member} -> {open_or_senior(member)}")