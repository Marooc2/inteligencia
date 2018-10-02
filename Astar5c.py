map_data = [
'######################################',
'#                         #          #',
'#       #  #  #  #         #   ####  #',
'#      #     #  #   ####  #    #  ####',
'## ###############  #     #    #     #',
'#     S          #  #     #          #',
'#        ###     #  #     #########  #',
'#  ##    #    ####  #     #      ##  #',
'#   #    #          #  G  #  #   #   #',
'#   ###  #          #        #   #   #',
'#        #          #        #       #',
'######################################',
]
map_width  = max([len(x) for x in map_data])
map_height = len(map_data)

class Node(object):  #tipo objeto
    start = None
    goal = None 
    def __init__(self,x,y):
        self.pos    = (x,y)
        self.hs     = (x-self.goal[0])**2 + (y-self.goal[1])**2
        self.fs     = 0
        self.owner_list  = None
        self.parent_node = None

    def isGoal(self):
        return self.goal == self.pos

class NodeList(list):
    def find(self, x,y):
        l = [t for t in self if t.pos==(x,y)]
        return l[0] if l != [] else None
    def remove(self,node):
        del self[self.index(node)]

for (i,x) in enumerate(map_data):
    if 'S' in x:
        Node.start = (x.index('S'),i)
    elif 'G' in x:
        Node.goal = (x.index('G'),i)

open_list     = NodeList()
close_list    = NodeList()
start_node    = Node(*Node.start)
start_node.fs = start_node.hs
open_list.append(start_node)

while True:
    if open_list == []:
        print("There is no route until reaching a goal.")
        exit(1);

    n = min(open_list, key=lambda x:x.fs)
    open_list.remove(n)
    close_list.append(n)

    if n.isGoal():
        end_node = n
        break

    #f*() = g*() + h*() -> g*() = f*() - h*()
    n_gs = n.fs - n.hs

    for v in ((1,0),(-1,0),(0,1),(0,-1)):
        x = n.pos[0] + v[0]
        y = n.pos[1] + v[1]

        if not (0 < y < map_height and
                0 < x < map_width and
                map_data[y][x] != '#'):
            continue

        m = open_list.find(x,y)
        dist = (n.pos[0]-x)**2 + (n.pos[1]-y)**2
        if m:
            if m.fs > n_gs + m.hs + dist:
                m.fs = n_gs + m.hs + dist
                m.parent_node = n
        else:
            m = close_list.find(x,y)
            if m:
                if m.fs > n_gs + m.hs + dist:
                    m.fs = n_gs + m.hs + dist
                    m.parent_node = n
                    open_list.append(m)
                    close_list.remove(m) 
            else:
                m = Node(x,y)
                m.fs = n_gs + m.hs + dist
                m.parent_node = n
                open_list.append(m)

n = end_node.parent_node
sol = [[x for x in line] for line in map_data]

while True:
    if n.parent_node == None:
        break
    sol[n.pos[1]][n.pos[0]] = '+'
    n = n.parent_node
print ("\n".join(["".join(x) for x in sol]))
