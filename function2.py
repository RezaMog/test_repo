def findpeaks(arr):
    """
    This function takes a list of numbers as input and returns the indices of the peaks in the list.
    
    A peak is defined as an element that is greater than its neighbors.
    
    Parameters:
    arr (list): A list of numbers.
    
    Returns:
    list: A list of indices where peaks are located.
    """
    peaks = []
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peaks.append(i)
    return peaks