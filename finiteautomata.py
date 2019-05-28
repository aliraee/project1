class finite_automata:

    def __init__(self, states = 0, alphabets = [], transitions = {}, init_state = 'q0', final_states = set()):
        self.states = states
        self.alphabets = alphabets
        self.transitions = transitions
        self.init_state = init_state
        self.final_states = final_states
    '''def __str__(self):
        return 'states:{0}\n alphabets:{1}\n transitions:{2}\n init_state:{3}\n final_state:{4} hhhhh'.format(self.states,self.alphabets,self.transitions,self.init_state,self.final_states)
    '''

def assign_data(file_path):
    s=''
    f=open(file_path,'r')
    for line in f:
        s+=line
    s=s.split('\n')
    lines=s
    #print(lines)
    nfa=finite_automata()
    
    states=lines[0]
    alphabets= lines[1].split(',')
    
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

t = assign_data('C:\\Users\\Asus\\Desktop\\code\\TheoryOfLanguagesAndMachines\\a.txt')

#f=open(path,'r')
'''s=''
for line in f:
    s+=line
s=s.split('\n')
print(s)'''
#t=assign_data(path)
#print(t)
#t = assign_data("D:\\uni\\Theory_of_langueges_and_machines\\a.txt")

def nfa_to_dfa(nfa):
    dfa = finite_automata(alphabets = nfa.alphabets)
    dfa_states = [ find_equal_states(nfa ,[nfa.init_state])]
    dfa.transitions["q0"] = []
    for states in dfa_states:
        
        next_states = {}
        for alphabet in nfa.alphabets:
            next_states[alphabet] = []
        for state in states:
            for transition in nfa.transitions[state]:
                
                if transition[0] != "_" and transition[1] not in next_states[transition[0]]:
                    next_states[transition[0]].append(transition[1])
        for next_state_list in next_states.values():
            next_state_list = find_equal_states(nfa, next_state_list)
            if next_state_list not in (dfa_states):
                dfa_states.append(next_state_list)
                for final_state in nfa.final_states:
                    if final_state in next_state_list:
                        dfa.final_states.add('q'+ str(dfa_states.index(next_state_list)))
                dfa.transitions['q'+ str(dfa_states.index(next_state_list))] = []

        for alphabet in next_states:
            dfa.transitions['q'+str(dfa_states.index(states))].append((alphabet,'q' + str(dfa_states.index(next_states[alphabet]))))
    dfa.states = len(dfa_states)
    return dfa
                    
def find_equal_states(automata, automata_states = []):
    for state in automata_states:
        for transition in automata.transitions[state]:
                if (transition[0] == "_" ):
                    automata_states.append(transition[1])
    automata_states.sort()
    return automata_states

dfa = nfa_to_dfa(t)

def write_automata_to_file(automata, file_path):
        f=open(file_path,'w')
        f.write(str(automata.states)+"\n")
        for alphabet in automata.alphabets[:-1]:
            f.write(alphabet+",")
        f.write(automata.alphabets[-1]+"\n")
        f.write("->")
        for state in automata.transitions:
            source_state = state
            if state in automata.final_states:
                source_state = "*"+source_state
            for dist_set in automata.transitions[state]:
                if dist_set[1] in automata.final_states:
                    dist_state = "*"+dist_set[1]
                else:
                    dist_state = dist_set[1]
                f.write(source_state+","+dist_set[0]+","+dist_state+"\n")
        f.close()
write_automata_to_file(dfa, "b.txt")




#pprint(t.transitions)
states=list(dfa.transitions.keys())
table=[]
final_state=list(dfa.final_states)
#final_state.sort()
final_states=dfa.final_states
for i in range(len(states)-1):
    for j in range(i+1,len(states)):
        #print(st[i],',',st[j])
        table.append([states[i],states[j],''])
for i in range(len(table)):
    if (table[i][0] in final_state and table[i][1] not in final_state) or(table[i][0] not in final_state and table[i][1]  in final_state):
        table[i][2]=1
#print(table)
for x in table:
    if x[2]=='':
        
        for alpha in dfa.alphabets:
            temp=[]
            for i in dfa.transitions[x[0]]:
                if i[0]==alpha:
                    temp.append(i[1])
                    break
            for i in dfa.transitions[x[1]]:
                if i[0]==alpha:
                    temp.append(i[1])
                    break
            temp.sort()
            for element in table:
                if element[0]==temp[0] and element[1]==temp[1] and element[2]==1:
                    x[2]=1
                    break
most_delete=[]
for i in table:
    if i[2]=='':
        most_delete.append(i[:-1])
#print(most_delete)
#element
for element in most_delete:
    dfa.transitions.pop(element[1],None)
    for el in dfa.transitions.keys():
        new_list=[]
        for x in dfa.transitions[el]:
            if element[1] in x:
                new_list.append((x[0],element[0]))
            else:
                new_list.append(x)
        dfa.transitions[el]=new_list

print(dfa.transitions)