from pyamaze import maze,agent,COLOR,textLabel
from queue import PriorityQueue
def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))
    
def aStar(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    open = PriorityQueue()
    open.put((h(start, m._goal), h(start, m._goal), start))
    aPath = {}
    g_score = {row: float("inf") for row in m.grid}
    g_score[start] = 0
    f_score = {row: float("inf") for row in m.grid}
    f_score[start] = h(start, m._goal)
    searchPath=[start]
    while not open.empty():
        currCell = open.get()[2]
        searchPath.append(currCell)
        if currCell == m._goal:
            break        
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, m._goal)

                if temp_f_score < f_score[childCell]:   
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_g_score + h(childCell, m._goal)
                    open.put((f_score[childCell], h(childCell, m._goal), childCell))


    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return searchPath,aPath,fwdPath

if __name__=='__main__':
    m=maze(4,4)
    m.CreateMaze(loadMaze='aStardemo.csv')

    searchPath,aPath,fwdPath=aStar(m)
    a=agent(m,footprints=True,color=COLOR.blue,filled=True)
    b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
    c=agent(m,footprints=True,color=COLOR.red)

    m.tracePath({a:searchPath},delay=300)
    m.tracePath({b:aPath},delay=300)
    m.tracePath({c:fwdPath},delay=300)

    l=textLabel(m,'A Star Path Length',len(fwdPath)+1)
    l=textLabel(m,'A Star Search Length',len(searchPath))
    m.run()



    # myMaze=maze(10,15)
    # myMaze.CreateMaze(6,4,loopPercent=100)

    # searchPath,aPath,fwdPath=aStar(myMaze,(1,12))


    # a=agent(myMaze,1,12,footprints=True,color=COLOR.blue,filled=True)
    # b=agent(myMaze,6,4,footprints=True,color=COLOR.yellow,filled=True,goal=(1,12))
    # c=agent(myMaze,1,12,footprints=True,color=COLOR.red,goal=(6,4))
    # myMaze.tracePath({a:searchPath},delay=200)
    # myMaze.tracePath({b:aPath},delay=200)

    # myMaze.tracePath({c:fwdPath},delay=200)

    # l=textLabel(myMaze,'A Star Path Length',len(fwdPath)+1)
    # l=textLabel(myMaze,'A Star Search Length',len(searchPath))

    # m.run()
