
<<<<<<< HEAD

import sys

def dfs(graph):
    visited = set()
    res = 0
    for u in graph.keys():
        if u not in visited:
            tree = set([u])
            edges = set()
            temp,l = dfs_visit(graph,visited,u,tree,edges)
            temp2 = 0
            for x in tree:
                for y in graph[x]:
                    if (x,y) not in edges and (y,x) not in edges:
                        temp2+=l[-1]
                        edges.add((x,y))
                        
            res+=temp+temp2
    return res
        
def dfs_visit(graph,visited,u,tree,edges):
    visited.add(u)
    res = 0
    l = []
    for v in graph[u]:
        if v in visited:
            continue
        tree.add(v)
        edges.add((u,v))
        res += (len(tree)-1)*len(tree)
        l.append((len(tree)-1)*len(tree))
        #print(res,tree,edges,l)
        t,lt = dfs_visit(graph,visited,v,tree,edges)
        res += t
        l.extend(lt)
    return res,l
    

t = int(input().strip())
for a0 in range(t):
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]
    graph = {}
    for a1 in range(m):
        x,y = input().strip().split(' ')
        x,y = [int(x),int(y)]
        #print(x,y)
        graph.setdefault(x,[y]).append(y)
        graph.setdefault(y,[x]).append(x)
    print(dfs(graph))
        # your code goes here
=======
def bfs(graph, start, visited, edges):
    q = [start]
    res = 0
    tree = set()
    last = 0
    while len(q):
        node = q.pop(0)
        visited.add(node)
        tree.add(node)
        #print(node,q,len(tree)*(len(tree)-1))
        last = len(tree)*(len(tree)-1)
        res += last
        for v in graph[node]:
            if v not in visited:
                visited.add(v)
                q.append(v)
                edges.add((node,v))
        #print(q)
    return res,last,tree,edges

def solve(graph):
    res = 0
    visited = set()
    edges = set()
    cc = []
    edges = set()
    lastSum = 0
    
    for u in graph.keys():
        if u not in visited:
            temp,last,tree,edg = bfs(graph,u,visited,edges)
            cc.append((temp,len(tree),last))
            
    cc.sort(reverse=True)
    
    for c in cc:
        temp = 0
        for i in range(c[1]):
            temp += i*(i+1)
            temp += lastSum if i>0 else 0
        lastSum += c[2]
        res += temp
    
    temp = 0
    loops = 0
    for u in graph.keys():
        for v in graph[u]:
            if (u,v) not in edges and (v,u) not in edges:
                loops+=1
                res += lastSum
                edges.add((u,v))
    print(loops,len(cc))
    return res

def from_file():
    f = open('graph.txt')
    t = int(f.readline().strip())
    for a0 in range(t):
        n,m = f.readline().strip().split(' ')
        n,m = [int(n),int(m)]
        graph = {}
        for x in range(1,n+1):
            graph[x]=[]
        for a1 in range(m):
            x,y = f.readline().strip().split(' ')
            x,y = [int(x),int(y)]
            graph.setdefault(x,[]).append(y)
            graph.setdefault(y,[]).append(x)
        #print 'read finished, solving'
        print(solve(graph))

def from_console():       
    t = int(input().strip())
    for a0 in range(t):
        n,m = input().strip().split(' ')
        n,m = [int(n),int(m)]
        graph = {}
        for x in range(1,n+1):
            graph[x]=[]
        for a1 in range(m):
            x,y = input().strip().split(' ')
            x,y = [int(x),int(y)]
            graph.setdefault(x,[]).append(y)
            graph.setdefault(y,[]).append(x)
        print(solve(graph))
>>>>>>> 8de2ea826650795d2792133fa28090a2d512b3c2
