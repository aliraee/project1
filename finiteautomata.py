from pprint import pprint
class finite_automata:
    def __init__(self, states = 0, alphabets = set(), transistions = {}, init_state = 'q0', final_states = set()):
        self.states = states
        self.alphabets = alphabets
        self.transitions = transistions
        self.init_state = init_state
        self.final_states = final_states
    '''def __str__(self):
        return 'states:{0}\n alphabets:{1}\n transitions:{2}\n init_state:{3}\n final_state:{4} hhhhh'.format(self.states,self.alphabets,self.transitions,self.init_state,self.final_states)
    '''

def assign_data(file_path):
    s=''
    f=open(path,'r')
    for line in f:
        s+=line
    s=s.split('\n')
    lines=s
    #print(lines)
    nfa=finite_automata()
    
    states=lines[0]
    alphabets=set(lines[1].split(','))
    
    init_transitions=[]
    init_state=lines[2].split(',')[0][2:]
    final_states=set()
    for i in range(2,len(lines)):
        t=(lines[i].split(','))
        init_transitions.append(t)
        if "*" in t[0] and t[0] not in final_states:
            final_states.add(t[0][1:])
    #pprint(init_transitions)
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
            if '*' in element[0][0]:
                element[0]=element[0][1:]
            if '*' in element[2][0]:
                element[2]=element[2][1:]
            result[element[0]]=[(element[1],element[2])]
        else:    
            if '*' in element[0][0]:
                element[0]=element[0][1:]
            if '*' in element[2][0]:
                element[2]=element[2][1:]
            result[element[0]]+=[(element[1],element[2])]
    #after done delete this line
    #pprint(result)
    return result
#test
#path='C:\\Users\\Asus\\Desktop\\code\\TheoryOfLanguagesAndMachines\\a.txt'
#f=open(path,'r')
'''s=''
for line in f:
    s+=line
s=s.split('\n')
print(s)'''
#t=assign_data(path)
#print(t)
