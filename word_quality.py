ENGLISH_FINGER_LAYOUT = {
            "`": 1,
            "1": 1,
            "q": 1,
            "a": 1,
            "z": 1,

            "2": 2,
            "w": 2,
            "s": 2,
            "x": 2,

            "3": 3,
            "e": 3,
            "d": 3,
            "c": 3,

            "4": 4,
            "r": 4,
            "f": 4,
            "v": 4,
            "5": 4,
            "t": 4,
            "g": 4,
            "b": 4,

            "6": 5,
            "y": 5,
            "h": 5,
            "n": 5,
            "7": 5,
            "u": 5,
            "j": 5,
            "m": 5,

            "8": 6,
            "i": 6,
            "k": 6,
            ",": 6,
            "<": 6,

            "9": 7,
            "o": 7,
            "l": 7,
            ".": 7,
            ">": 7,

            "0": 8,
            "p": 8,
            ";": 8,
            "/": 8,
            "?": 8,
            "-": 8,
            "_": 8,
            "=": 8,
            "+": 8,
            "[": 8,
            "{": 8,
            "]": 8,
            "}": 8,
            "\\": 8,
            "|": 8,
            "'": 8,
            '"': 8,
}

def word_quality(word, layout=1):
    finger_layout = {}

    # English QWERTY finger layout
    if layout == 1:
        finger_layout = ENGLISH_FINGER_LAYOUT
    # Persian ISIRI finger layout
    elif layout == 2:
        raise NotImplementedError("Persian layout is not implemented yet")

    # Rules:
    # weight fingers
    # using the same finger twice in a row is bad

    # Finger weights
    finger_weights = {
        1: 1,
        2: 3,
        3: 3.5,
        4: 5,
        5: 5,
        6: 3.5,
        7: 3,
        8: 1,
    }

    # Measure some statistics
    finger_usage = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    double_finger_usage = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }

    # Calculate finger usage and double finger usage
    for i in range(len(word)):
        letter = word[i]
        finger = finger_layout[letter]
        
        # Count the finger usage
        finger_usage[finger] += 1

        # Check if the previous letter was used with the same finger
        if i > 0:
            if finger == finger_layout[word[i - 1]]:
                double_finger_usage[finger] += 1
    
    # Calculate the quality of the word
    quality = 0
    for finger in finger_usage:
        quality += finger_weights[finger] * finger_usage[finger]

    # Subtract the double finger usage
    for finger in double_finger_usage:
        quality -= double_finger_usage[finger] * (6 - finger_weights[finger])
    
    # Normalize the quality
    quality /= len(word)
    
    return finger_usage, double_finger_usage, quality



if __name__ == "__main__":
    print("Press 1 for English(QWERTY) and 2 for Persian(ISIRI) layout")
    layout = int(input())

    if layout == 1:
        print("Enter the word: ", end="")
    elif layout == 2:
        print("Enter the word: ", end="")
    else:
        print("Invalid layout")
        exit()

    # Get the word from user
    word = input()
    word = word.lower()
    word = word.replace(" ", "")

    # Calculate the quality of the word
    finger_usage, double_finger_usage, quality = word_quality(word, layout)

    # Print the quality
    print(f"> Quality: {quality: .3f}")
    print()

    finger_layout = ENGLISH_FINGER_LAYOUT if layout == 1 else ENGLISH_FINGER_LAYOUT
    # Sort the finger usage
    finger_usage = sorted(finger_usage.items(), key=lambda x: x[1], reverse=True)
    print("> Finger usage:")
    for finger in finger_usage:
        characters = [ch for ch in word if finger_layout[ch] == finger[0]]
        print(finger[0], ":", finger[1], f"[{' '.join(characters)}]")
    print()

    # Sort the double finger usage
    double_finger_usage = sorted(double_finger_usage.items(), key=lambda x: x[1], reverse=True)
    print("> Double finger usage:")
    for finger in double_finger_usage:
        print(finger[0], ":", finger[1])
