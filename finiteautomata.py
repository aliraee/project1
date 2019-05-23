from pprint import pprint
class finite_automata:
    def __init__(self, states = [], alphabets = [], transistions = {}, init_state = 'q0', final_states = []):
        self.states = states
        self.alphabets = alphabets
        self.transitions = transistions
        self.init_state = init_state
        self.final_states = final_states
   # def __str__(self):
   #     return 'states:{0}\n alphabets:{1}\n transitions:{2}\n init_state:{3}\n final_state:{4} hhhhh'.format(self.states,self.alphabets,self.transitions,self.init_state,self.final_states)


def assign_data(file_lines):
    lines=file_lines
    nfa=finite_automata()
    states=lines[0]
    alphabets=lines[1].split(',')
    
    init_transitions=[]
    init_state=lines[2].split(',')[0][2:]
    final_states=[]
    for i in range(2,len(lines)):
        t=(lines[i].split(','))
        init_transitions.append(t)
        if "*" in t[0] and t[0] not in final_states:
            final_states.append(t[0])
    transitions=make_transitions(init_transitions)
    nfa.states=states
    nfa.alphabets=alphabets
    nfa.init_state=init_state
    nfa.final_states=final_states
    nfa.transitions=transitions
    return nfa

def assign_data(file_lines):
    lines=file_lines
    #print(lines)
    nfa=finite_automata()
    
    states=lines[0]
    alphabets=lines[1].split(',')
    
    init_transitions=[]
    init_state=lines[2].split(',')[0][2:]
    final_states=[]
    for i in range(2,len(lines)):
        t=(lines[i].split(','))
        init_transitions.append(t)
        if "*" in t[0] and t[0] not in final_states:
            final_states.append(t[0])
    transitions=make_transitions(init_transitions)
    nfa.states=states
    nfa.alphabets=alphabets
    nfa.init_state=init_state
    nfa.final_states=final_states
    nfa.transitions=transitions
    return nfa

def make_transitions(lst):
    #TODO make transitions with doctionary
    result={}
    
    result[lst[0][0][2:]]=[(lst[0][1],lst[0][2])]

    #result[x[0][2:]]=[(x[1],x[2][:-1])]
    for element in lst[1:]:
        if element[0] not in result.keys():
            result[element[0]]=[(element[1],element[2])]
        else:    
            
            result[element[0]]+=[(element[1],element[2])]
    #after done delete this line
    #pprint(result)
    return result
#test
'''path='C:\\Users\\Asus\\Desktop\\code\\TheoryOfLanguagesAndMachines\\a.txt'
f=open(path,'r')
s=''
for line in f:
    s+=line
s=s.split('\n')'''
#print(s)
#t=assign_data(s)
#print(t)
