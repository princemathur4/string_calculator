class StringCalc:
    @staticmethod
    def add(numbers: str) -> int:
        if not isinstance(numbers, str):
            raise Exception("Invalid input - [numbers]")

        if not numbers:
            return 0

        return sum(map(int, numbers.split(",")))
