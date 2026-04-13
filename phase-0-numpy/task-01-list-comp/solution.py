# Task 1
def squares_of_evens(n):
    return [x*x for x in range(n) if x % 2 == 0]


# Task 2
def label_temperatures(temps):
    return ['freezing' if x <= 0 else
            'cold' if x <= 15 else
            'warm' if x <= 25 else
            'hot'
            for x in temps]


# Task 3
def filter_long_words(words, min_len):
    return [word.upper() for word in words if len(word) > min_len]


# Task 4
def flatten_pairs(pairs):
    return [item for sublist in pairs for item in sublist]


if __name__ == '__main__':
    print(squares_of_evens(10))
    print(label_temperatures([0, 1, 15, 16, 25, 26, 15.5]))
    print(filter_long_words(["cat", "dog", "fish"], 3))
    print(flatten_pairs([(1, 2), (3, 4), (5, 6)]))