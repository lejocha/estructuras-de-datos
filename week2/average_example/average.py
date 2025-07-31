def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return avrage

if __name__ == "__main__":
    data = []
    print("The average is:", calculate_average(data))
