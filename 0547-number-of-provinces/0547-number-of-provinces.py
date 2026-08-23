class Solution:
    def dfs(self,i,AdjMatrix,visited):
        visited[i]=True
        for x in range(len(AdjMatrix)):
            if AdjMatrix[i][x]==1 and not visited[x]:
                self.dfs(x,AdjMatrix,visited)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        ans=0
        for i in range(n):
            if not visited[i]:
                self.dfs(i,isConnected,visited)
                ans+=1
        return ans
        