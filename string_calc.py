class StringCalc:
    @staticmethod
    def add(numbers: str) -> int:
        if not isinstance(numbers, str):
            raise Exception("Invalid input - [numbers]")

        if not numbers:
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            delimiter = numbers.split("\n")[0].lstrip("//")
            numbers = "\n".join(numbers.split("\n")[1:])

        numbers = numbers.replace("\n", delimiter)
        return sum(map(int, numbers.split(delimiter)))
