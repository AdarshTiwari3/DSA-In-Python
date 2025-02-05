class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        tiles=sorted(tiles)
        def helper(seen):

            total_ways=0
            for i in range(len(tiles)):
                if seen[i]:
                    continue #skip the element
                if i > 0 and tiles[i] == tiles[i-1] and not seen[i-1]:
                    continue

                seen[i]=True
                total_ways+=1
                total_ways+=helper(seen)
                #backtrack
                seen[i]=False

            return total_ways


        seen=[False]*len(tiles)
        return helper(seen)

