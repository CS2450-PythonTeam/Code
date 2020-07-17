# UVSim.py
# This file can contain the main loop

class VM:
    def __init__(self, program):
        self.accumulator = 0
        self.memory = [0]*100
        self.pc = 0
        self.running = True
        self.opcode = {
            10: self.read,
            11: self.write,
        }
    
    def __call__():
        while running:
            pass
            #read from mem[pc]
            #parse instruction
            #execute instruction
            #increment pc
    
    def read_char(addr):
        '''
        use this to read a character from memory
        '''
    
    def write_char(addr, char):
        '''
        use this to write a character to memory
        '''
    
    def read_word(addr):
        '''
        use this to read an int
        '''
    
    def write_word(addr, word):
        '''
        use this to write an int
        '''
    
    def debug(addr):
        '''
        prints out the accumulator, program counter and memory.
        '''
    
    def read(self, addr):
        '''
        reads a character from the keyboard
        '''
        return
    
    def write(self, addr)
        '''
        writes a character to the screen
        '''

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()