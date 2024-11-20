def sort(numbers):
    # Implementing Bubble Sort
    # returns sorted list in ascending order
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # swap adjacent elements
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

#calculate the median of the sorted list
#returns a float value (median value)
def sortAndFindMedian(numbers):
    sorted_numbers = sort(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        # find the avaerage of the two middle values
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        # assign median to the middle value
        median   = sorted_numbers[n // 2]
    return median

def main():
    # Main function to read input, process the data, and display the median
    print("Enter numbers separated by spaces:")
    numbers = list(map(int, input().split()))
    # call the sortAndFindMedian recrusively
    median = sortAndFindMedian(numbers)
    print(f"Median: {median}")

if __name__ == "__main__":
    main()
