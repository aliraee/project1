from finiteautomata import *

path='C:\\Users\\Asus\\Desktop\\code\\TheoryOfLanguagesAndMachines\\a.txt'

dfa=nfa_to_dfa(dfa)
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

print(dfa.tra)