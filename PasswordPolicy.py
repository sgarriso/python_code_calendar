class PasswordPolicy:
    def __init__(self, pair:str, symbol, text):
        result = pair.split('-')
        self.min, self.max = int(result[0]), int(result[1])
        self.symbol = symbol[:-1]
        self.text  = text
        self.counter = self.counts()
    def counts(self):
        data = {}
        data[self.symbol] = 0
        for char in self.text:
            if char in data:
                data[char] = data[char] + 1
            else:
                data[char] = 1
        return data
    def is_valid(self):
        result = self.counter[self.symbol] 
        return self.min <= result  <= self.max
    def is_valid_other(self):
        return (self.text[self.min - 1] == self.symbol) is not (self.text[self.max - 1 ] == self.symbol)
        
    
    def __repr__(self):
        return f"{self.min} {self.max} {self.symbol}  {self.text} {self.counter}  {self.is_valid_other()}"
        