class NoSuchTransitionError(Exception):
	def __init__(self, start_state, end_state):
		super().__init__("The transition "+start_state+"->"+end_state+" does not exist in this machine")
		self.start_state = start_state
		self.end_state = end_state