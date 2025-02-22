def find_min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    return min(left_min, right_min), max(left_max, right_max)


if __name__ == "__main__":
    numbers = [13, 3, 20, 32, 8, 0, 26, 17]
    min_val, max_val = find_min_max(numbers)

    print("Numbers:", numbers)
    print(f"Min: {min_val}")
    print(f"Max: {max_val}")
