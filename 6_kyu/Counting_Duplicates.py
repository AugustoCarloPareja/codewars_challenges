## Solution 1
def duplicate_count_1(text):
        chars = []
        repeated = []

        for char in text:
            if char.lower() not in chars:
                chars.append(char.lower())
            else:
                if char.lower() not in repeated:
                    repeated.append(str(char.lower()))
        return len(repeated)

## Solution 2
def duplicate_count_2(text):
    text = text.lower()
    repeated_chars = []
    
    for char in text:
        if text.count(char) > 1 and char not in repeated_chars:
            repeated_chars.append(char)
    return len(repeated_chars)

if __name__ == '__main__':
    texts = [
        'K97aQqVLBAIMJheWuJzN0ZNLwIrqBgK',
        'UsbvaqX76BO918UjMzD1WxnDPeqk7ChAlB2AZI',
        'obnvS4QHzqjOdDLKMtzaKVH7i9TztNU4G8leZP7lNKb',
        'K79X60YlpwMrOcSmfbo6xpEWZvbHJJMIrCralWVuviglD4KiKxcQyhm0QfYtOfhEatnjyh3xHO4UvcSZ774aVqVfA'
        ]
    
    for text in texts:
        print(
            f"""
            Solution 1:
            The lenght of '{text}' is {duplicate_count_1(text)}
            
            Solution 2:
            "The lenght of '{text}' is {duplicate_count_2(text)}
            """
            )