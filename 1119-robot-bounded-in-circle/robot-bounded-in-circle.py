class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        distances = [0,0,0,0]

        for i in instructions:
            if i == "L":
                direction = (direction -1 ) % 4
            elif i == "R":
                direction = (direction + 1) % 4
            else:
                distances[direction] +=1
        if (distances[0] == distances[2] and distances[1] == distances[3]) or (direction != 0):
            return True
        else:return False
        