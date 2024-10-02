import unittest

from FiniteStateMachine import FiniteStateMachine

class TestFiniteStateMachine(unittest.TestCase):
	def test_happy(self):
		fsm = FiniteStateMachine(["state1", "state2"])
		fsm.add_transition("state1","state2",on_transition=lambda: print("forward transition"))
		fsm.add_transition("state2","state1",on_transition=lambda:print("backwards transition"))
		fsm.transition_state("state1")
		fsm.transition_state("state2")
		fsm.transition_state("state1")
