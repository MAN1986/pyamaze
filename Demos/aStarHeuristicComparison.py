from aStarDemo import aStar
from aStarDemo2 import aStar2
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

# myMaze=maze(30,40)
# myMaze.CreateMaze(loopPercent=100)
# searchPath,aPath,fwdPath=aStar(myMaze)
# searchPath2,aPath2,fwdPath2=aStar2(myMaze)

# l=textLabel(myMaze,'Manhattan',len(fwdPath)+1)
# l=textLabel(myMaze,'Euclidean',len(fwdPath2)+1)
# l=textLabel(myMaze,'Manhattan',len(searchPath)+1)
# l=textLabel(myMaze,'Euclidean',len(searchPath2)+1)

# a=agent(myMaze,footprints=True,color=COLOR.cyan,filled=True)
# b=agent(myMaze,footprints=True,color=COLOR.yellow)
# myMaze.tracePath({a:fwdPath},delay=50)
# myMaze.tracePath({b:fwdPath2},delay=50)

# t1=timeit(stmt='aStar(myMaze)',number=100,globals=globals())
# t2=timeit(stmt='aStar2(myMaze)',number=100,globals=globals())

# textLabel(myMaze,'Manhattan Time',t1)
# textLabel(myMaze,'Euclidean Time',t2)


# myMaze.run()

f1,f2,f3=0,0,0
s1,s2,s3=0,0,0

for _ in range(100):
    myMaze=maze(20,30)
    myMaze.CreateMaze(loopPercent=100)
    searchPath,aPath,fwdPath=aStar(myMaze)
    searchPath2,aPath2,fwdPath2=aStar2(myMaze)

    if len(fwdPath)==len(fwdPath2):
        f1+=1
    elif len(fwdPath)<len(fwdPath2):
        f2+=1
    else:
        f3+=1

    if len(searchPath)==len(searchPath2):
        s1+=1
    elif len(searchPath)<len(searchPath2):
        s2+=1
    else:
        s3+=1

print('Final Path Comparison Result') 
print(f'Both have same Final Path length for {f1} times.')
print(f'Manhattan has lesser Final Path length for {f2} times.')
print(f'Euclidean has lesser Final Path length for {f3} times.')

print('--------------------------------------------')

print('Search Path Comparison Result')
print(f'Both have same Search Path length for {s1} times.')
print(f'Manhattan has lesser Search Path length for {s2} times.')
print(f'Euclidean has lesser Search Path length for {s3} times.')