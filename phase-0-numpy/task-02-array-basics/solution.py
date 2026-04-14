import numpy as np


# Task 1
def create_checkerboard(n=3):
    arr = np.zeros((int(n), int(n)), dtype=np.int8)
    arr[0::2, 1::2] = 1
    arr[1::2, 0::2] = 1
    return arr


# Task 2
def memory_footprint(shape, dtype):
    dt = np.dtype(dtype)
    item_size = dt.itemsize
    size = np.prod(shape)
    ndim = len(shape)
    nbytes = size * item_size

    def human(nbytes):
        units = 'B', 'KB', 'MB', 'GB', 'TB'
        value = float(nbytes)

        for unit in units:
            if value < 1024.0 or unit == units[-1]:
                return f'{round(value, 2)} {unit}'
            value /= 1024.0
        return None

    return {
        "shape": tuple(shape),
        "ndim": ndim,
        "size": size,
        "dtype": dt.name,
        "nbytes": nbytes,
        "nbytes_human": human(nbytes)
    }


# Task 3
def safe_normalize(img):
    if img.dtype == np.uint8:
        # Нормализация из [0, 255] → [0.0, 1.0]
        return img.astype(np.float32) / 255.0

    elif img.dtype == np.float32:
        # Проверяем, что значения уже в диапазоне [0, 1]
        if img.min() >= 0.0 and img.max() <= 1.0:
            return img.copy()
        else:
            raise ValueError(
                "float32 input must have values in range [0.0, 1.0]"
            )

    else:
        raise ValueError(
            f"Unsupported dtype: {img.dtype}. Expected uint8 or float32."
        )


# Task 4
def linspace_vs_arange_demo():
    lin = np.linspace(0, 1, 11)      # гарантированно 11 точек
    arr = np.arange(0, 1, 0.1)       # "примерно" 0..1 с шагом 0.1

    return lin, arr


# Task 5
def reshape_to_batch(flat_pixels, h, w, c, n):
    expected_size = n * h * w * c
    actual_size = flat_pixels.size

    if actual_size != expected_size:
        raise ValueError(
            f"Expected size {expected_size}, but got {actual_size}"
        )
    return flat_pixels.reshape((n, h, w, c))