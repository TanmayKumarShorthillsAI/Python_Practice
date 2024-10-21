class Solution:
    count = 0

    def dfs(self, s, rooms, visited):
        visited[s] = True
        self.count += 1

        for x in rooms[s]:
            if not visited[x]:
                self.dfs(x, rooms, visited)

    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        if n == 0:
            return True
        visited = [False] * n

        self.dfs(0, rooms, visited)

        if self.count != n:
            return False

        return True
