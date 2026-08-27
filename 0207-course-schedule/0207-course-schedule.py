class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adjList=[]*n
        ans=[]
        incoming=[0]*n
        q=[]
        for i in range(n):
            adjList.append([])
        for a,b in prerequisites:
            incoming[a]+=1
            adjList[b].append(a)
        for i in range(n):
            if incoming[i]==0:
                ans.append(i)
                q.append(i)
        while q:
            front=q.pop(0)
            for x in adjList[front]:
                incoming[x]-=1
                if incoming[x]==0:
                    ans.append(x)
                    q.append(x)
        return len(ans)==n