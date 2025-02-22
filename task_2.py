import random


def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):
        return quick_select(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    else:
        return quick_select(right, k - len(left) - len(mid))


if __name__ == "__main__":
    numbers = [13, 3, 20, 32, 8, 0, 26, 17]
    k = 3

    print("Numbers:", numbers)
    kth_element = quick_select(numbers, k)
    print(f"{k}-th min: {kth_element}")
