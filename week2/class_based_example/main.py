from utils.calculator import AverageCalculator
from models.dataset import get_sample_data

if __name__ == "__main__":
    data = get_sample_data()
    calculator = AverageCalculator()
    result = calculator.calculate(data)
    print("Average is: " + result)  # Bug: TypeError, mixing str + float
