class finite_automata:
    def __init__(self, states = [], alphabets = [], transistions = {}, init_state = 'q0', final_states = []):
        self.states = states
        self.alphabets = alphabets
        self.transitions = transistions
        self.init_state = init_state
        self.final_states = final_states
    
