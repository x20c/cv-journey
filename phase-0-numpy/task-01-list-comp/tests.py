from solution import squares_of_evens, label_temperatures, filter_long_words, flatten_pairs


def test_squares_of_evens():
    print('Testing Happy Path! Task 1')
    assert squares_of_evens(3) == [0, 4], f'Happy path not good! We need to have 0, 4'
    assert squares_of_evens(11) == [0, 4, 16, 36, 64, 100], 'Happy path not good! We need to have 0, 4, 16, 36, 64, 100'
    assert squares_of_evens(1) == [0], 'Happy Path not good! We need to have 0'
    assert squares_of_evens(2) == [0], 'Happy Path not good! We need to have 0'
    print('Testing Edge Case! Task 1')
    assert squares_of_evens(0) == [], 'Edge Case not good! We need to have an empty list'



def test_label_temperatures():
    print('Testing Edge Case! Task 2')
    assert label_temperatures([]) == [], 'Edge case not good! We need to have an empty list'
    print('Testing Happy Path! Task 2')
    assert label_temperatures([1]) == ['cold'], 'Happy path not good! We need to have cold'
    assert label_temperatures([0, 14, 17, 22, 33]) == ['freezing', 'cold', 'warm', 'warm', 'hot'], 'Happy path not good! We waiting freezing, cold, warm, hot'
    assert label_temperatures([15, 16, 25, 26]) == ['cold', 'warm', 'warm', 'hot'], 'Happy path not good! We waiting cold, warm, warm, hot'
    print('Testing Boundary values! Task 2')
    assert label_temperatures([-0.19964, 0.5, -0.5, -222.9]) == ['freezing', 'cold', 'freezing', 'freezing'], 'Boundary Values not good! We waiting freezing cold freezing freezing'
    assert label_temperatures([0.9, 15.51, 25.1, 26.24324]) == ['cold', 'warm', 'hot', 'hot'], 'Boundary Values not good! We waiting cold warm hot hot'

def test_filter_long_words():
    print('Testing Edge Case! Task 3')
    assert filter_long_words([], 0) == [], 'Edge Case not good! We need to have an empty list'
    assert filter_long_words(['1'], 0) == ['1'], 'Edge Case not good! We need to have 1'
    print('Testing Happy Path! Task 3')
    assert filter_long_words(['hello', 'how', 'hwee'], 4) == ['HELLO'], 'Happy Path not good! We need to have HELLO'
    print('Testing Boundary values! Task 3')
    assert filter_long_words(['hehe', 'aza', 'qweqw', 'aOa', 'zwein'], 3) == ['HEHE', 'QWEQW', 'ZWEIN'], 'Boundary Values not good!'
    assert filter_long_words(['ad' ,'hehe', 'aza', 'qweqw', 'aOa', 'zwein'], 3.5) == ['HEHE', 'QWEQW', 'ZWEIN'], 'Boundary Values not good!'

def test_flatten_pairs():
    print('Testing Edge Case! Task 4')
    assert flatten_pairs([]) == [], 'Edge Case not good! We need have noting.'
    assert flatten_pairs([(0, 0)]) == [0, 0], 'Edge Case not good! We need to have 0,0'
    assert flatten_pairs([(0, )]) == [0, ], 'Edge Case not good! We need to have 0, '
    assert flatten_pairs([(None, 1)]) == [None, 1], 'Edge Case not good! We need to have None, 1'
    print('Testing Happy Path! Task 4')
    assert flatten_pairs([(1,2), (3,5), (6, 6)]) == [1, 2, 3, 5, 6, 6], 'Happy Path not good! We need to have 1, 2, 3, 5, 6, 6'
    assert flatten_pairs([(1,2), (3 , )]) == [1, 2, 3, ], 'Happy Path not good! We need to have 1, 2, 3, '


if __name__ == "__main__":
    test_squares_of_evens()
    test_label_temperatures()
    test_filter_long_words()
    test_flatten_pairs()
    print("All tests passed ✓")