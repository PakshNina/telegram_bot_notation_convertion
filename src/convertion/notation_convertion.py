class ConvertNotation:
    def __init__(self):
        self.target_base = 2
        self.from_base = 10

    def number_to_base(self, number, from_base=None, base=None):
        if number == '0':
            return number
        self.target_base = base if base else self.target_base
        self.from_base = from_base if from_base else self.from_base
        try:
            if isinstance(number, str):
                number = int(number, self.from_base)
        except ValueError:
            raise ValueError('Укажите систему исчисления у числа')
        sign = '-' if number < 0 else ''
        number = abs(number)
        result = ''
        while number >= self.target_base:
            result = str(number % self.target_base) + result
            number = number // self.target_base
        if number > 0:
            result = str(number) + result
        if sign:
            result = '-' + result
        return result
