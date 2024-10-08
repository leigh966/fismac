import unittest
from parameterized import parameterized
from FiniteStateMachine import FiniteStateMachine
from NoSuchStateError import NoSuchStateError
from NoSuchTransitionError import NoSuchTransitionError

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
	@parameterized.expand([
		[["state1","state2"], [("state1","state2")], ("state2", "state1")],
		[["state1","state2"], [("state2","state1")], ("state1", "state2")]
	])
	def test_none_existent_transition(self, all_states, all_transitions, transition_to_try):
		fsm = FiniteStateMachine(all_states, transition_to_try[0])
		for transition in all_transitions:
			fsm.add_transition(transition[0],transition[1])
			print("added transition",transition[0],"->",transition[1])
		print(fsm.get_current_state())
		self.assertRaises(NoSuchTransitionError, lambda:fsm.transition_state(transition_to_try[1]))

