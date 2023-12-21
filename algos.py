from Pyamaze import *
from collections import deque
from queue import PriorityQueue
import time
def DFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSeacrh=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        dSeacrh.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dSeacrh,dfsPath,fwdPath

def BFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    bSearch=[]

    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
                bSearch.append(childCell)
    
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bSearch,bfsPath,fwdPath

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))
def ASTAR(m,start=None):
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
  
def run_maze(grid_size,initial_pos,goal_pos,selected_algo) :
    m = maze(grid_size[0],grid_size[1])
    m.CreateMaze(goal_pos[0],goal_pos[1],loopPercent=60)
    start = 0
    end = 0
    if selected_algo == 'DFS' :
        start = time.time()
        search_space,backwordPath,forwardPath=DFS(m,initial_pos)
        end = time.time()
    elif selected_algo == 'BFS':
        start = time.time()
        search_space,backwordPath,forwardPath=BFS(m,initial_pos)
        end = time.time()
    elif selected_algo == 'A*' :
        start = time.time()
        search_space,backwordPath,forwardPath=ASTAR(m,initial_pos)
        end = time.time()
    else :
        timesRequired = {}
        l=textLabel(m,f'Estimation Chart','DFS,BFS,A*',(1200,20),(685,100),18)

        l=textLabel(m,'Name','',(1200,140),(165,50),18)
        l=textLabel(m,'BFS','',(1375,140),(165,50),18)
        l=textLabel(m,'DFS','',(1550,140),(165,50),18)
        l=textLabel(m,'A*','',(1725,140),(165,50),18)
        start = time.time()
        dfs_search_space,dfs_backwordPath,dfs_forwardPath = DFS(m,initial_pos)
        end = time.time()
        timesRequired['DFS'] = f'{round((end-start)*1000,3)} ms'
        start = time.time()
        bfs_search_space,bfs_backwordPath,bfs_forwardPath = BFS(m,initial_pos)
        end = time.time()
        timesRequired['BFS'] = f'{round((end-start)*1000,3)} ms'
        start = time.time()
        astar_search_space,astar_backwordPath,astar_forwardPath = ASTAR(m,initial_pos)
        end = time.time()
        timesRequired['A*'] = f'{round((end-start)*1000,3)} ms'

        ## for dfs
        dfs_a=agent(m,initial_pos[0],initial_pos[1],goal=goal_pos,footprints=True,shape='square',color=COLOR.yellow)
        dfs_b=agent(m,goal_pos[0],goal_pos[1],goal=initial_pos,footprints=True,filled=True,color=COLOR.blue)
        dfs_c=agent(m,initial_pos[0],initial_pos[1],footprints=True,color=COLOR.red)
        m.tracePath({dfs_a:dfs_search_space},showMarked=True,delay=150)
        m.tracePath({dfs_b:dfs_backwordPath},delay=150)
        m.tracePath({dfs_c:dfs_forwardPath},delay=150)
        ## for bfs
        bfs_a=agent(m,initial_pos[0],initial_pos[1],goal=goal_pos,footprints=True,shape='square',color=COLOR.green)
        bfs_b=agent(m,goal_pos[0],goal_pos[1],goal=initial_pos,footprints=True,filled=True,color=COLOR.cyan)
        bfs_c=agent(m,initial_pos[0],initial_pos[1],footprints=True,color=COLOR.yellow)
        m.tracePath({bfs_a:bfs_search_space},showMarked=True,delay=150)
        m.tracePath({bfs_b:bfs_backwordPath},delay=150)
        m.tracePath({bfs_c:bfs_forwardPath},delay=150)   
        ## for a*
        astar_a=agent(m,initial_pos[0],initial_pos[1],goal=goal_pos,footprints=True,shape='square',color=COLOR.blue)
        astar_b=agent(m,goal_pos[0],goal_pos[1],goal=initial_pos,footprints=True,filled=True,color=COLOR.red)
        astar_c=agent(m,initial_pos[0],initial_pos[1],footprints=True,color=COLOR.green)
        m.tracePath({astar_a:astar_search_space},showMarked=True,delay=150)
        m.tracePath({astar_b:astar_backwordPath},delay=150)
        m.tracePath({astar_c:astar_forwardPath},delay=150) 
        l=textLabel(m,'Path Length','',(1200,210),(165,50),16)
        l=textLabel(m,'B',f'{len(bfs_forwardPath)+1}',(1375,210),(165,50),18)
        l=textLabel(m,'D',f'{len(dfs_forwardPath)+1}',(1550,210),(165,50),18)
        l=textLabel(m,'A',f'{len(astar_forwardPath)+1}',(1725,210),(165,50),18)  
        l=textLabel(m,'Search Space','',(1200,280),(165,50),14)
        l=textLabel(m,'B',f'{len(bfs_search_space)}',(1375,280),(165,50),18)
        l=textLabel(m,'D',f'{len(dfs_search_space)}',(1550,280),(165,50),18)
        l=textLabel(m,'A',f'{len(astar_search_space)}',(1725,280),(165,50),18) 
        l=textLabel(m,'Required Time','',(1200,350),(165,50),14)
        l=textLabel(m,'B',f'{timesRequired["BFS"]}',(1375,350),(165,50),18)
        l=textLabel(m,'D',f'{timesRequired["DFS"]}',(1550,350),(165,50),18)
        l=textLabel(m,'A',f'{timesRequired["A*"]}',(1725,350),(165,50),18)                 
        m.run()
    a=agent(m,initial_pos[0],initial_pos[1],goal=goal_pos,footprints=True,shape='square',color=COLOR.green)
    b=agent(m,goal_pos[0],goal_pos[1],goal=initial_pos,footprints=True,filled=True)
    c=agent(m,initial_pos[0],initial_pos[1],footprints=True,color=COLOR.yellow)
    m.tracePath({a:search_space},showMarked=True,delay=150)
    m.tracePath({b:backwordPath},delay=150)
    m.tracePath({c:forwardPath},delay=150)
    l=textLabel(m,f'{selected_algo} Path Length',len(forwardPath)+1,(1200,50),(600,100),28)
    l=textLabel(m,f'{selected_algo} Search Length',len(search_space),(1200,185),(600,100),28)
    l=textLabel(m,f'{selected_algo} Time Taken',f'{round((end-start)*1000,3)} ms',(1200,320),(600,100),28)
    m.run()
