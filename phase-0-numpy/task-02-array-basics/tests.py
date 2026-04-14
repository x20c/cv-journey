from solution import create_checkerboard, memory_footprint, safe_normalize, reshape_to_batch, linspace_vs_arange_demo
import numpy as np


def test_create_checkerboard():
    print('Testing Task 1')
    assert create_checkerboard(4).shape == (4, 4), 'We waiting 4, 4'
    assert create_checkerboard(15).shape == (15, 15), 'We waiting 15, 15'
    assert create_checkerboard(224).shape == (224, 224), 'We waiting 224, 224'
    assert create_checkerboard(3.5).shape == (3, 3), 'We waiting 3, 3'
    assert create_checkerboard().shape == (3, 3), 'We waiting 3, 3'
    print('All tests passed! Task 1')


def test_memory_footprint():
    print('Testing Task 2')
    res = memory_footprint((2, 3), np.int8)

    assert res["shape"] == (2, 3), 'We waiting 2, 3'
    assert res["ndim"] == 2, 'We waiting 2'
    assert res["size"] == 6, 'We waiting 6'
    assert res["dtype"] == "int8", 'We waiting int8'
    assert res["nbytes"] == 6, 'We waiting 6'  # 6 элементов * 1 байт
    assert res["nbytes_human"] == "6.0 B", 'We waiting 6.0 B'

    res = memory_footprint((2, 2), np.float32)

    assert res["size"] == 4, f'We waiting 4'
    assert res["dtype"] == "float32", 'We waiting float32'
    assert res["nbytes"] == 16, 'We waiting 16'  # 4 * 4 байта

    res = memory_footprint((4, 5, 6), np.int16)

    assert res["ndim"] == 3, 'We waiting 3'
    assert res["size"] == 120, 'We waiting 120'
    assert res["nbytes"] == 240, 'We waiting 240'  # 120 * 2 байта

    res = memory_footprint((1024,), np.int8)

    # 1024 B → 1 KB
    assert res["nbytes"] == 1024, 'We waiting 1024'
    assert res["nbytes_human"] == "1.0 KB", 'We waiting 1.0 KB'
    print('All tests passed! Task 2')


def test_safe_normalize():
    print('Testing Task 3')
    img = np.array([0, 127, 255], dtype=np.uint8)
    res = safe_normalize(img)

    expected = np.array([0.0, 127 / 255, 1.0], dtype=np.float32)

    assert res.dtype == np.float32, 'We waiting float32'
    assert np.allclose(res, expected), f'We waiting {res}, expected {expected}'

    img = np.array([-0.1, 0.5, 1.1], dtype=np.float32)

    try:
        safe_normalize(img)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert "range [0.0, 1.0]" in str(e)

    img = np.array([0, 1, 2], dtype=np.int32)

    try:
        safe_normalize(img)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert "Unsupported dtype" in str(e)
    print('All tests passed! Task 3')


def test_linspace_vs_arange_demo():
    print('Test task 4!')
    res = linspace_vs_arange_demo()

    # это кортеж длины 2
    assert isinstance(res, tuple), 'Error test!'
    assert len(res) == 2, 'We waiting 2'

    lin, arr = res

    # оба — ndarray
    assert isinstance(lin, np.ndarray)
    assert isinstance(arr, np.ndarray)

    # linspace строго 11 элементов
    assert lin.size == 11, 'We waiting 11'

    # arange — проверяем фактическое значение
    assert arr.size == 10, 'We waiting 10'
    print('All tests passed! Task 4')


def test_reshape_to_batch():
    print('Testing Task 5')
    flat = np.arange(24)
    res = reshape_to_batch(flat, h=2, w=3, c=2, n=2)

    assert res.shape == (2, 2, 3, 2), 'We waiting 2, 2, 3, 2'
    assert np.array_equal(res.flatten(), flat), 'Error!'

    flat = np.arange(8)
    res = reshape_to_batch(flat, 2, 2, 1, 2)

    expected = np.array([
        [[[0], [1]],
         [[2], [3]]],

        [[[4], [5]],
         [[6], [7]]]
    ])

    assert np.array_equal(res, expected), f'We waiting {res}, expected {expected}'

    flat = np.arange(12, dtype=np.float32)
    res = reshape_to_batch(flat, 2, 2, 3, 1)

    assert res.dtype == np.float32, 'We waiting float32'
    assert res.shape == (1, 2, 2, 3), 'We waiting (1, 2, 2, 3)'
    print('All tests passed! Task 5')


if __name__ == '__main__':
    test_create_checkerboard()
    test_memory_footprint()
    test_safe_normalize()
    test_reshape_to_batch()
    test_linspace_vs_arange_demo()