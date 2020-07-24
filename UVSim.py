# UVSim.py
# This file can contain the main loop
# Michael Elliott et al Summer 2020
import sys

class VM:
    def __init__(self):
        self.accumulator = 0
        self.memory = [0]*100
        self.pc = 0
        self.running = True
        self.operation = None
        self.operand = None
        self.instructor = {
            10: self.read,
            11: self.write,
            20: self.load,
            21: self.store,
            30: self.add,
            31: self.subtract,
            32: self.divide,
            33: self.multiply,
            40: self.branch,
            41: self.branchneg,
            42: self.branchzero,
            43: self.halt
        }
    
    def __call__(self):
        while self.running:
            #read the instruction and increment pc
            instruction = abs(self.memory[self.pc])
            self.pc += 1

            #parse the instruction
            self.operation = instruction//100
            self.operand = instruction%100

            #execute the instruction
            self.instructor[self.operation](self.operand)
    
    def hand_loader(self):
        print("*** Welcome to UVSim ***")
        print("*** Please enter your program one instruction    ***")
        print("*** ( or data word ) at a time into the input    ***")
        print("*** text field. I will display the location      ***")
        print("*** number and a question mark (?). You then     ***")
        print("*** type the word for that location. Enter       ***")
        print("*** -99999 to stop entering your program.        ***")
        addr = 0
        instruction = 0
        while instruction != -99999:
            instruction = int(input(f'{addr} ? '))
            if 10000 > instruction > -10000:
                self.memory[addr] = instruction
            addr += 1
        print("***  Program loading completed    ***")
        print("***  Program execution beings     ***")

    def __overflow(self, number):
        '''
        The internal silent overflow
        '''
        if abs(number)//10000 > 0:
            return 0-(number%10000)
        return number
    
    def debug(self):
        '''
        prints out the accumulator, program counter and memory.
        '''
        print("REGISTERS:          None")
        print(f"Accumulator:        {self.accumulator}")
        print(f"InstructionCounter: {self.pc}")
        print(f"OperandCode:        {self.operation}")
        print(f"Operand:            {self.operand}" )
        print('0\t1\t2\t3\t4\t5\t6\t7\t8\t9')
        count = 0
        for x in range(0,9):
            print(f"{str(x*10).zfill(2)}\t",end='')
            for y in range(0,9):
                print(f"{str(self.memory[x*10+y]).zfill(5)}\t",end='')
            print()

    
    def read(self, addr):
        '''
        reads a integer from the keyboard
        '''
        self.memory[addr] = self.__overflow(int(input("Enter an integer: ")))
    
    def write(self, addr):
        '''
        writes a integer to the screen
        '''
        print(f"Contense of {addr} is {self.memory[addr]}")
    
    def load(self, addr):
        '''
        loads a word from memory
        '''
        self.accumulator = self.memory[addr]

    def store(self, addr):
        '''
        stores a word into memory
        '''
        self.memory[addr] = self.accumulator
    
    def add(self, addr):
        '''
        adds the number in the accumulator to the address
        '''
        self.accumulator = self.__overflow(self.memory[addr]+ self.accumulator)

    def subtract(self, addr):
        '''
        subtracts the number in the accumulator from the address
        '''
    
    def divide(self, addr):
        '''
        divides the number in the accumulator by the address
        '''
    
    def multiply(self, addr):
        '''
        multiplies the number in the accumulator by the address
        '''
    
    def branch(self, addr):
        '''
        branches the program to the address
        '''
        self.pc = addr
    
    def branchneg(self, addr):
        '''
        branches the program to the address
        only if the accumulator is negitive
        '''
    
    def branchzero(self, addr):
        '''
        branches the program to the address
        only if the accumulator is zero
        '''
    
    def halt(self, addr):
        self.running = False
        print("*** Simpletron execution terminated ***")
        self.debug()

def main():
    vm = VM()
    vm.hand_loader()
    vm()

if __name__ == "__main__":
    main()
