n = int(input())  
instructions = [input().strip() for _ in range(n)]

stack = []
register = 0
pc = 0  

while pc < len(instructions):
    instr = instructions[pc].split()

    if instr[0] == "PUSH":
        value = int(instr[1])
        stack.insert(0, value)  
        pc += 1

    elif instr[0] == "STORE":
        register = stack.pop(0)
        pc += 1

    elif instr[0] == "LOAD":
        stack.insert(0, register)
        pc += 1

    elif instr[0] == "PLUS":
        a = stack.pop(0)
        b = stack.pop(0)
        stack.insert(0, a + b)
        pc += 1

    elif instr[0] == "TIMES":
        a = stack.pop(0)
        b = stack.pop(0)
        stack.insert(0, a * b)
        pc += 1

    elif instr[0] == "IFZERO":
        target = int(instr[1])
        value = stack.pop(0)
        if value == 0:
            pc = target
        else:
            pc += 1

    elif instr[0] == "DONE":
        print(stack[0])
        break
