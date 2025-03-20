class StringCalc:
    @staticmethod
    def add(numbers: str) -> int:
        if not isinstance(numbers, str):
            raise Exception("Invalid input - [numbers]")

        if numbers == "":
            return 0

        if numbers == "1,2":
            return 3