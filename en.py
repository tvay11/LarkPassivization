from lark import Lark, Tree, Transformer

def passive(parser, program):
    parse_tree = parser.parse(program)
    l= program.split(" ")
    count=0
    a=[]
    b=[]
    for inst in parse_tree.children: #MAKING THE ARRAY
            m=[]
            listType=[]
            for rootChildren in inst.children:
                 rootC = []
                 if(len(rootChildren.children)==0): #for single word (verb, prep
                        m.append([l[count]])
                        count += 1
                 if(len(rootChildren.children)>0): #for phrase
                    for ui in rootChildren.children:
                        if(len(ui.children)>0): #checking if they have children
                            inter=[]
                            for io in ui.children:
                                qv = []
                                if(len(io.children)>0):
                                    for qq in io.children: #for to in po
                                        qv.append(l[count])
                                        count+=1
                                else: #for name in vo
                                    inter.append(l[count])
                                    count+=1
                            rootC.append(inter)
                            if(qv): #for ordering po
                                rootC.append(qv)
                        else:#na in no
                            rootC.append(l[count])
                            count+=1
                 if(rootC):
                    m.append(rootC)
                 listType.append(rootChildren.data+'')
            a.append([inst.data+'',m])
            b.append([inst.data+'',listType])

    prepHere=False
    for we in a: #CHANGING STUFF HERE
        if(we[0]=="no"):
            indexNo=we.index(we[1])
            indexNoX=a.index(we)
            we[indexNo][indexNoX].insert(0,"by")
            copier = we[1]
        elif(we[0]=="vo"):
            for lp in b:
                for ll in lp[1]:
                    if(ll=="verb"):
                        indexVerb=lp[1].index(ll)
                        indexVerbx=a.index(we)
                        if (we[indexVerbx][indexVerb]==["gives"]):
                            we[indexVerbx][indexVerb]=["received"]
                        elif (we[indexVerbx][indexVerb]==["shares"]):
                            we[indexVerbx][indexVerb]=["shared"]
                        elif (we[indexVerbx][indexVerb]==["eats"]):
                            we[indexVerbx][indexVerb]=["ate"]
                        elif (we[indexVerbx][indexVerb]==["drinks"]):
                            we[indexVerbx][indexVerb]=["drank"]
                        elif (we[indexVerbx][indexVerb]==["buys"]):
                            we[indexVerbx][indexVerb]=["gave"]
                    elif(ll=="no"):
                            indexNewNo=lp[1].index(ll)
                            indexNewNoX=a.index(we)
                            if(len(we[indexNewNoX][indexNewNo])>1): # for po in o
                                qs=[]
                                for kp in range(1,len(we[indexNewNoX][indexNewNo])):
                                    qs.append(we[indexNewNoX][indexNewNo][kp])
                                we[indexNewNoX].append(qs)
                                copier2=[we[indexNewNoX][indexNewNo][0]]

                            else:
                                copier2 = we[indexNewNoX][indexNewNo]
                    elif(ll=="prep"):
                        prepHere=True
                        indexPrep=lp[1].index(ll)
                        indexPrepX=a.index(we)
                        if(we[indexPrepX][indexPrep]==['with']):
                            a[0][indexNo][indexNoX][0]='with'
    #switcher
    a[indexNoX][indexNo]=copier2
    a[indexNewNoX][1][indexNewNo]=copier

    if(prepHere): #remove prep and add it to verb
        a[indexPrepX][1].remove(a[indexPrepX][1][indexPrep])

    abc=""
    for build in a: #BUILDING IT BACK
        if(build[0]=="no"):
           jl=build[1]
           for tt in jl:
               for lo in tt:
                abc=abc+" "+lo
        if(build[0])=="vo":
           jl=build[1]
           for tt in jl:
               for lo in tt:
                   if(isinstance(lo,list)): # for na in vo
                        tip=lo
                        for nn in tip:
                            abc=abc+" "+nn
                   else:
                       abc=abc+" "+lo
    abc=abc[1:]
    return abc


my_grammar=("""

start: no vo | po no vo 
no: na |na po 
na: name det adj* thing
po: prep stuff | prep thing |prep det* adj* place | prep det* adj* place to | to 
to: prep* det* time* 
vo: verb so prep no 
so: det adj* stuff
det: "the" | "a" | "an"
name: "Mary"|"Patricia"|"Barbara"|"Linda"|"Elizabeth"|"Maria"|"Jennifer"|"Betty"|"Helen"|"James"| "John"| "Robert"| "Michael"| "William"| "David"| "Richard"| "Charles"| "Joseph"| "Thomas"| "George"| "Steven"| "Edward"| "Brian" 
stuff: "food" | "toy" | "bottle" | "clothes"| "toothbrush" | "gum" | "pizza" | "hamburger" 
thing: "duck" | "dog"| "cat"| "rabbit"| "hamster"| "fish"| "bird"| "lizard"| "turtle"| "tiger"| "shark"| "zebra"| "crab"| "lobster" | "fox"
verb: "gives" | "buys" |"shares"| "eats" | "drinks " |  "received" | "shared" | "ate" | "drank" | "gave"|
prep: "with" | "to"  | "on" | "from" | "in" | "at" | "during" 
adj: "big" | "little" | "angry"| "calm" | "old" | "young" | "kind" | "mean" | "nice" | "unique" 
place:"home" | "farm" | "barn" | "school" | "ocean" | "house" 
time: "tommorow" | "now" | "evening" |"afternoon" | "morning" | "dawn" | "sunset" 

%import common.WORD
%ignore " "

""")

corpus = """ """

parser=Lark(my_grammar)
for sent in corpus[1:].split('\n'):
  print("=======\nsentence:",sent)
  try:
   print("passivization:", passive(parser,sent))
  except:
    print('No valid Parse.')

