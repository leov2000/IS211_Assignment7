import os
import sys
import unittest

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../'))

from die import Die 

class TestDie(unittest.TestCase):
    
    def setUp(self):
        self.die_piece = Die()
    
    def test_die_roll_has_side_state(self):
        die_num = self.die_piece.roll_the_die()

        self.assertEqual(isinstance(die_num, int), True)

    def test_die_roll_has_num_between_1_and_6(self):
        die_num = self.die_piece.roll_the_die()

        self.assertTrue(die_num in range(1,7), True)

    def test_die_side_reset(self):
        self.die_piece.reset_die_side()
        (side, count) = self.die_piece.get_die_state()

        self.assertEqual(side, 0)

    def test_die_counter_reset(self):
        self.die_piece.reset_roll_count()
        (side, count) = self.die_piece.get_die_state()

        self.assertEqual(count, 0)

    def test_die_has_full_state(self):
        self.die_piece.roll_the_die()
        state_tuple = self.die_piece.get_die_state()

        self.assertNotEqual(state_tuple, ())

