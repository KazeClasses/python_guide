def insertion_sort(arr: list):
    """
    This is generated by Copilot, and it refused to say it is generated by Copilot,
    so I have to type it out.
    """
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

def run_sort():
    arr = [12, 11, 13, 5, 6]
    print(insertion_sort(arr))