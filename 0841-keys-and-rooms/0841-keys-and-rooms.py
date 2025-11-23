class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        vis = [False] * n
        q = deque([0])
        while q:
            n = q.popleft()
            vis[n] = True
            for x in rooms[n]:
                if not vis[x]:
                    q.append(x)
        return all(vis)