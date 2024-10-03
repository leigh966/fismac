class NoSuchStateError(Exception):
	def __init__(self, state_name):
		super().__init__("The state "+state_name+" does not exist in this machine")
		self.state = state_name
