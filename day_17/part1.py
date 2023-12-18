from heapq import heappop, heappush


with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
MAP = [[int(i) for i in list(j)] for j in lines]
ROW_COUNT = len(MAP)
COL_COUNT = len(MAP[0])
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


queue = [(0, (0, 0), (0, 0), 0)]
visited = {((0, 0), (0, 0)): 0}
stop = False


while stop == False:
    cost, position, direction, steps = heappop(queue)
    if position == (ROW_COUNT-1, COL_COUNT-1):
        stop = True
        result = cost
    
    else:
        for dir in DIRECTIONS:
            if (direction != dir) and (direction != (-dir[0], -dir[1])):
                next_cost = cost
                for movement in range(1, 4):
                    next_position = (position[0]+dir[0]*movement, position[1]+dir[1]*movement)
                    if next_position[0] >= 0 and next_position[0] < ROW_COUNT and next_position[1] >= 0 and next_position[1] < COL_COUNT:
                        next_cost += MAP[next_position[0]][next_position[1]]
                        if (next_position, dir) in visited.keys():
                            if next_cost < visited[(next_position, dir)]:
                                visited[(next_position, dir)] = next_cost
                                heappush(queue, (next_cost, next_position, dir, movement))
                        else:
                            visited[(next_position, dir)] = next_cost
                            heappush(queue, (next_cost, next_position, dir, movement))
print(result)