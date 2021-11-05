def dijkstra(graph,start,goal):
    unvisited={n:float('inf') for n in graph.keys()}
    unvisited[start]=0
    visited={}
    revPath={}

    while unvisited:
        minNode=min(unvisited, key=unvisited.get)
        visited[minNode]=unvisited[minNode]

        if minNode==goal:
            break

        for neighbor in graph.get(minNode):
            if neighbor in visited:
                continue
            tempDist=unvisited[minNode]+graph[minNode][neighbor]
            if tempDist < unvisited[neighbor]:
                unvisited[neighbor]=tempDist
                revPath[neighbor]=minNode
        
        unvisited.pop(minNode)
    node=goal
    revPathString=node
    while node!=start:
        revPathString+=revPath[node]
        node=revPath[node]
    fwdPath=revPathString[::-1]
    return fwdPath, visited[goal]


if __name__=='__main__':
    myGraph={
        'A':{'B':2, 'C':9, 'F':4},
        'B':{'C':6, 'E':3, 'F':2},
        'C':{'D':1},
        'D':{'C':2},
        'E':{'D':5,'C':2},
        'F':{'E':3}
    }

    startNode='A'
    goalNode='D'
    path,cost=dijkstra(myGraph,startNode,goalNode)
    print(f'The cost to reach from {startNode} to {goalNode} is {cost}.')
    print(f'The path is : {path}')
