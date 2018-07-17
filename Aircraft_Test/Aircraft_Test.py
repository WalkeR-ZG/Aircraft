import unittest
from Aircraft.Aircraft import Aircraft
from Aircraft.domain.Position import Position


class AircraftTest(unittest.TestCase):
    def setUp(self):
        self.aircraft = Aircraft()

    def set_position(self, position):
        self.aircraft.set_position(position)

    def exec_instruction(self, instruction):
        self.aircraft.run(instruction)

    def should_at_position(self, position):
        self.assertEqual(self.aircraft.get_position(), position)


class TestInitPosition(AircraftTest):
    def test_init_position(self):
        self.should_at_position(Position(0, 0, 0, 'N'))


class TestUpDownForward(AircraftTest):
    def test_up_down_forward(self):
        self.set_position(Position(0, 0, 5, 'N'))
        self.exec_instruction('UP')
        self.should_at_position(Position(0, 0, 6, 'N'))
        self.exec_instruction('DOWN')
        self.should_at_position(Position(0, 0, 5, 'N'))
        self.exec_instruction('FORWARD')
        self.should_at_position(Position(0, 1, 5, 'N'))


class TestLeftRoundRight(AircraftTest):
    def test_left_round_right(self):
        self.exec_instruction('LEFT')
        self.should_at_position(Position(0, 0, 0, 'W'))
        self.exec_instruction("ROUND")
        self.should_at_position(Position(0, 0, 0, 'E'))
        self.exec_instruction('RIGHT')
        self.should_at_position(Position(0, 0, 0, 'S'))


class TestRepeatUpN(AircraftTest):
    def test_repeat_up_n(self):
        self.exec_instruction('REPEAT(UP_N(3), 2)')
        self.should_at_position(Position(0, 0, 6, 'N'))

if __name__ == '__main__':
    unittest.main()
