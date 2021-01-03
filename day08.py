import copy

NOT_VISITED = -1

class Instruction:

    def __init__(self, cmd, value):
        self.cmd = str(cmd)
        self.value = int(value)
        self.reset()
        
    def reset(self):
        self.visited = NOT_VISITED

    @property
    def executed(self):
        return self.visited != NOT_VISITED
    
    
class Program:
    """Boot sequence"""
    def __init__(self, instructions):
        self._instructions = instructions
        self.reset()

    def __len__(self):
        return len(self._instructions)
        
    def __getitem__(self, index):
        return self._instructions[index]

    def reset(self):
        [instruction.reset() for instruction in self._instructions]
        self.accumulator = 0
        self.state = 0
        self.trace = []

    def execute(self, instruction):
        """Change accumulator (if necessary) and return new offset. 
        """
        if instruction.cmd == 'jmp':
            return instruction.value
        if instruction.cmd == 'acc':
            self.accumulator += instruction.value
        return 1
    
    def __next__(self):
        """Single executation step: fetch instruction, check if already
        excuted, if yes: terminate, if no: execute. 
        """
        if self.state >= len(self):
            raise StopIteration('Terminated')
        
        instruction = self[self.state]
        # entering infinite loop
        if instruction.executed:
            raise StopIteration('Crashed')

        instruction.visited = len(self.trace)
        self.trace.append(self.state)
        self.state += self.execute(instruction)

    def __iter__(self):
        self.reset()
        return self

    @property
    def status(self):
        try:
            next(self)
            return 'Running'
        except StopIteration as err:
            return err.value

        
def read_program(filename):
    """Read boot sequence from file. 
    """
    with open(filename) as handle:
        lines = [line for line in handle.read().split('\n') if line]
    return Program([Instruction(*line.split()) for line in lines])


if __name__ == '__main__':

    filename = 'input08.txt'
    program = read_program(filename)

    # run program until it crashes 
    list(program)
    print('{0} with accumulator = {1}'.format(
        program.status, program.accumulator))
    
    # try to fix code
    fixes = {'jmp': 'nop', 'nop': 'jmp'}
    
    while len(program.trace):
        state = program.trace.pop()
        instruction = program[state]
        if instruction.cmd not in fixes:
            continue
        testprog = copy.deepcopy(program)
        testprog[state].cmd = fixes[instruction.cmd]
        testprog.state = state
        list(testprog)
        if testprog.status == 'Terminated':
            break

    print('Terminated after fix with accumulator =',
          testprog.accumulator)

