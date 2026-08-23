from heapq import heappush,heappop
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], s: int) -> Dict[int, int]:
        adjList=[]
        for i in range(n):
            adjList.append([])
        for edge in edges:
            a,b,c=edge[0],edge[1],edge[2]

            adjList[a].append([b,c])
        heap=[]
        ans={}
        for i in range(n):
            ans[i]=float('inf')

        ans[s]=0
        heappush(heap,(ans[s],s))
        while heap:
            d,u=heappop(heap)
            for v,w in adjList[u]:
                if ans[u]+w<ans[v]:
                    ans[v]=ans[u]+w
                    heappush(heap,(ans[v],v))
        for i in ans:
            if ans[i]==float('inf'):
                ans[i]=-1
        return ans