from domain.Position import Position
from domain.Instruction import InstructionFactory


class Aircraft:
    def __init__(self):
        self.position = Position(0, 0, 0, 'N')

    def run(self, instruct):
        InstructionFactory().create_instruction(instruct).run(self.position)

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position
