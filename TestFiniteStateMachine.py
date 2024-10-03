import unittest
from parameterized import parameterized
from FiniteStateMachine import FiniteStateMachine
from NoSuchStateError import NoSuchStateError
class TestFiniteStateMachine(unittest.TestCase):
	def test_happy(self):
		fsm = FiniteStateMachine(["state1", "state2"])
		fsm.add_transition("state1","state2",on_transition=lambda: print("forward transition"))
		fsm.add_transition("state2","state1",on_transition=lambda:print("backwards transition"))
		fsm.transition_state("state1")
		print(fsm.get_current_state())
		fsm.transition_state("state2")
		print(fsm.get_current_state())
		fsm.transition_state("state1")
		print(fsm.get_current_state())
	@parameterized.expand([
		[["state1"], "state2", "state1"],
		[["state1","state2"], "state1", "state3"]
	])
	def test_add_transition_missing(self, all_states, from_state, to_state):
		fsm = FiniteStateMachine(all_states)
		self.assertRaises(NoSuchStateError, lambda:fsm.add_transition(from_state, to_state)) 
