import re


class Instruction(object):
    def run(self, position):
        pass


class UpInstruction(Instruction):
    def run(self, position):
        position.up()


class DownInstruction(Instruction):
    def run(self, position):
        position.down()


class ForwardInstruction(Instruction):
    def run(self, position):
        position.forward()


class TurnInstruction(Instruction):
    def __init__(self, left):
        self.turn = left

    def run(self, position):
        position.turn_to(self.turn)


class CompositeInstruction(Instruction):
    def __init__(self, instruction, exec_times=1):
        self.instruction = instruction
        self.exec_times = exec_times

    def run(self, position):
        for index in range(0, self.exec_times, 1):
            self.instruction.run(position)


class InstructionFactory(object):
    ATOMIC_INSTRUCTION_DICT = {
        'UP': UpInstruction(),
        'DOWN': DownInstruction(),
        'FORWARD': ForwardInstruction(),
        'LEFT': TurnInstruction(True),
        'RIGHT': TurnInstruction(False),
        'ROUND': CompositeInstruction(TurnInstruction(False), 2),
    }

    COMPOSITE_INSTRUCTION_DICT = {
        'UP_N': ["(.+?)\_", "\((.+?)\)"],
        'DOWN_N': ["(.+?)\_", "\((.+?)\)"],
        'FORWARD_N': ["(.+?)\_", "\((.+?)\)"],
        'REPEAT': ["\((.+?)\,", "\,(.+?)\)"]
    }

    def create_instruction(self, instruction_str):
        instruction_str = instruction_str.strip()
        if instruction_str in self.ATOMIC_INSTRUCTION_DICT.keys():
            return self.ATOMIC_INSTRUCTION_DICT.get(instruction_str)
        else:
            return self.__create_composite_instruction(instruction_str)

    def __create_composite_instruction(self, instruction_str):
        composite_instruction = re.findall("(.+?)\(", instruction_str)[0]
        if composite_instruction in self.COMPOSITE_INSTRUCTION_DICT.keys():
            regular_expression = self.COMPOSITE_INSTRUCTION_DICT.get(composite_instruction)
            instruction = re.findall(regular_expression[0], instruction_str)[0]
            times = int(re.findall(regular_expression[1], instruction_str)[0])
            return CompositeInstruction(self.create_instruction(instruction), times)
        else:
            raise IOError("no this instruction")
