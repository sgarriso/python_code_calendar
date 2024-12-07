
class StateMachine:

# Initialize 
    def start(self):
        self.state = self.startState
        self.result = ""
        self.table = []
        self.number_string = ""
        self.enable = True

# Step through the input
    def step(self, inp:str):
        (s, o) = self.getNextValues(self.state, inp)

        if o:
            self.result = self.result + inp
        else:
            self.result = ""
        if s == 6:
            if self.enable:
                self.table.append(self.result)
            else:
                self.result = ""
            s = 0
            self.result = ""

        self.state = s
    def process_nums(self, inp:str):
        (s, o) = self.getNextValues(self.state, inp)
        if (self.state == 4 or self.state == 5) and inp.isnumeric():
            self.number_string = self.number_string + inp
        if inp == ')' or inp == ',':
            self.table.append(int(self.number_string))
            self.number_string = ""
        self.state = s
                
             

# Loop through the input		
    def feeder(self, inputs):
        self.start()
        for inp in inputs:
            self.step(inp) 
        return self.table
    def feeder_2(self, inputs):
        self.start()
        for inp in inputs:
            self.process_nums(inp) 
        return self.table

# Determine the TRUE or FALSE state
class TextSeq(StateMachine):
    startState = 0
    def getNextValues(self, state, inp:str):
        if state == 0 and inp == 'm':
            return (1, True)
        elif state == 1 and inp == 'u':
            return (2, True)
        elif state == 2 and inp == 'l':
            return (3, True)
        elif state == 3 and inp == '(':
            return (4, True)
        elif state == 4 and inp.isnumeric():
            return (4, True)
        elif state == 4 and inp == ',':
            return (5, True)
        elif state == 5 and inp.isnumeric():
            return (5, True)
        elif state == 5 and inp == ')':
            return (6, True)
        elif state == 0 and inp == 'd':
            return (10, False)
        elif state == 10 and inp == 'o':
            return (11, False)
        elif state == 11 and inp == '(':
            return (12, False)
        elif state == 12 and inp == ')':
            self.enable = True
            return (0, False)
        elif state == 11 and inp == 'n':
            return (21, False)
        elif state == 21 and inp == "'":
            return (22, False)
        elif state == 22 and inp == 't':
            return (23, False)
        elif state == 23 and inp == '(':
            return (24, False)
        elif state == 24 and inp == ')':
            self.enable = False
            return (0, False)
        
        else:
            return (0, False)
