class AverageCalculator:
    def calculate(self, numbers):
        # Bug: forget to check for empty list
        total = 0
        for n in numbers:
            total += n
        return total / len(numbers)  # Bug: misspelled variable
