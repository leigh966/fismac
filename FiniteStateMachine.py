class State():
	_transitions = {}
	def __init__(self, name, on_enter=None, on_exit=None):
		self.name = name
		self.on_enter = on_enter
		self.on_exit = on_exit
	def add_transition(self, target_state, on_transition=None):
		self._transitons[target_state.name]={"obj":target_state,"on_transition":on_transition}
	def do_transtion(target_state):
		if self.on_exit is not None:
			self.on_exit()
		action = _transition
		if action is not None:
			action()
class FiniteStateMachine:
	_current_state = None
	_states = {}
	def __init__(self, state_names=[], start_state=None):
		for name in state_names:
			add_state(name)
	def add_state(state_name):
		_states[state_name] = State(state_name)
		return self
	def add_transition(from_state, to_state, on_transition=None):
		from_state_obj = get_state(from_state)
		to_state_obj = get_state(to_state)
		from_state_obj.add_transition(to_state_obj, on_transition)
	def get_state(state_name):
		for state in _states:
			if state.name == state_name:
				return state
		return None
	def transition_state(new_state_name):
		new_state = get_state(new_state_name)
		if current_state is not None:
			current_state.do_transition(new_state)
		current_state = new_state
		if current_state.on_enter is not None:
			current_state.on_enter()
