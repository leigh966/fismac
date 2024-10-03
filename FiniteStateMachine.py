from NoSuchStateError import NoSuchStateError
from NoSuchTransitionError import NoSuchTransitionError
class State():
	def __init__(self, name, on_enter=None, on_exit=None):
		self._transitions = {}
		self.name = name
		self.on_enter = on_enter
		self.on_exit = on_exit
	def add_transition(self, target_state, on_transition=None):
		self._transitions[target_state.name]={"obj":target_state,"on_transition":on_transition}
	def do_transition(self,target_state):
		if self.on_exit is not None:
			self.on_exit()
		if target_state.name not in self._transitions: # this is coming back false when it shouldn't
			raise NoSuchTransitionError(self.name, target_state.name) 
		action = self._transitions[target_state.name]["on_transition"]
		if action is not None:
			action()

			
class FiniteStateMachine:
	def __init__(self, state_names=[], start_state=None):
		self._states = {}
		for name in state_names:
			self.add_state(name)
		self._current_state = None
		if start_state is not None:
			self.transition_state(start_state)
			
	def add_state(self,state_name):
		self._states[state_name] = State(state_name)
		return self
	def get_state_or_throw(self,state_name):
		out = self.get_state(state_name)
		if out is None:
			raise NoSuchStateError(state_name)
		return out
	def add_transition(self,from_state, to_state, on_transition=None):
		from_state_obj = self.get_state_or_throw(from_state)
		to_state_obj = self.get_state_or_throw(to_state)
		from_state_obj.add_transition(to_state_obj, on_transition)
	def get_state(self,state_name):
		if state_name in self._states:
			return self._states[state_name]
		return None
	def transition_state(self, new_state_name):
		new_state = self.get_state(new_state_name)
		if self._current_state is not None:
			self._current_state.do_transition(new_state)
		self._current_state = new_state
		if self._current_state.on_enter is not None:
			self._current_state.on_enter()
	def get_current_state(self):
		return self._current_state.name
