class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        c=0
        rs,cs=0,0
        re,ce=len(matrix)-1,len(matrix[0])-1
        total=len(matrix)*len(matrix[0])
        ans=[]
        while c<total:
            for i in range(cs,ce+1):
                ans.append(matrix[rs][i])
                c+=1
            rs+=1
            if c==total:
                break
            for i in range(rs,re+1):
                ans.append(matrix[i][ce])
                c+=1
            ce-=1
            if c==total:
                break
            for i in range(ce,cs-1,-1):
                ans.append(matrix[re][i])
                c+=1
            re-=1
            if c==total:
                break
            for i in range(re,rs-1,-1):
                ans.append(matrix[i][cs])
                c+=1
            cs+=1
            if c==total:
                break
        return ans