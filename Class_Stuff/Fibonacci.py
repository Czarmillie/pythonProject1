class Fibonacci:
    def __init__(self):
        pass

    def Fibonacci_series(self, counter):
        first_number = 0
        second_number = 1
        series = [0] * counter
        series[0] = first_number

        if counter > 1:
            series[1] = second_number
            for num in range(2, counter):
                next_number = first_number + second_number
                series[num] = next_number
                first_number = second_number
                second_number = next_number

        return series

if __name__ == "__main__":
    fibonacci = Fibonacci()
    counter = 10
    series = fibonacci.Fibonacci_series(counter)
    print("Fibonacci series:", series)
