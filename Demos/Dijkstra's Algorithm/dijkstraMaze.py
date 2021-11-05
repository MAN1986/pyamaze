from pyamaze import maze,agent,COLOR,textLabel
def dijkstra(m,*h,start=None):
    if start is None:
        start=(m.rows,m.cols)

    hurdles=[(i.position,i.cost) for i in h]

    unvisited={n:float('inf') for n in m.grid}
    unvisited[start]=0
    visited={}
    revPath={}
    while unvisited:
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]
        if currCell==m._goal:
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                for hurdle in hurdles:
                    if hurdle[0]==currCell:
                        tempDist+=hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        unvisited.pop(currCell)
    
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    
    return fwdPath,visited[m._goal]
            



if __name__=='__main__':
    myMaze=maze(10,15)
    myMaze.CreateMaze(1,4,loopPercent=100)
    # myMaze.CreateMaze(loadMaze='dijkMaze.csv')

    h1=agent(myMaze,4,4,color=COLOR.red)
    h2=agent(myMaze,4,6,color=COLOR.red)
    h3=agent(myMaze,4,1,color=COLOR.red)
    h4=agent(myMaze,4,2,color=COLOR.red)
    h5=agent(myMaze,4,3,color=COLOR.red)

    h1.cost=100
    h2.cost=100
    h3.cost=100
    h4.cost=100
    h5.cost=100

    # path,c=dijstra(myMaze,h1,h2,h2,h3,h4,h5)
    path,c=dijkstra(myMaze,h1,h2,h3,h4,h5,start=(6,1))
    textLabel(myMaze,'Total Cost',c)

    # a=agent(myMaze,color=COLOR.cyan,filled=True,footprints=True)
    a=agent(myMaze,6,1,color=COLOR.cyan,filled=True,footprints=True)
    myMaze.tracePath({a:path})


    myMaze.run()