class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        
        rows = defaultdict(int) #stores the count of lamps on row
        cols = defaultdict(int) #stores the count of lamps on col
        primary = defaultdict(int) #  diagonal 1
        secondary = defaultdict(int) # diagonal 2
        lamp_set = set() #tracks the position of lamp
        # store the rows , cols & diagonals where bulbs are on.
        for i, j in lamps: 
            if (i, j) not in lamp_set:
                lamp_set.add((i, j))
                rows[i] += 1
                cols[j] += 1
                primary[i+j] += 1
                secondary[i-j] += 1

        for i, j in queries:
            if rows[i] or cols[j] or primary[i+j] or secondary[i-j]: #check the all directions i.e row , col , both diagonals
                res.append(1)
            else:
                res.append(0)
            #turn off the first lamp then to check the other one
            for delrow in range(i-1, i+2):
                for delcol in range(j-1, j+2):
                    if (delrow, delcol) in lamp_set:
                        lamp_set.remove((delrow, delcol))
                        rows[delrow] -= 1
                        cols[delcol] -= 1
                        primary[delrow+delcol] -= 1
                        secondary[delrow-delcol] -= 1
        return res