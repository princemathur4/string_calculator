class StringCalc:
    @staticmethod
    def add(numbers: str) -> int:
        if not isinstance(numbers, str):
            raise Exception("Invalid input for param(s) = [numbers]")

        if not numbers:
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            delimiter = numbers.split("\n")[0].lstrip("//")
            numbers = "\n".join(numbers.split("\n")[1:])

        numbers = numbers.replace("\n", delimiter)

        try:
            numbers_list = list(map(int, numbers.split(delimiter)))
        except ValueError:
            raise Exception("Invalid delimiter present in param(s) = [numbers]")

        negative_numbers = list(filter(lambda num: num < 0, numbers_list))
        if negative_numbers:
            raise Exception(f"Negative numbers not allowed: [{negative_numbers[0]}]")
        return sum(numbers_list)
