class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        def dfs(sr, sc, visited, image):
            for direction in directions:
                new_sr = sr + direction[0]
                new_sc = sc + direction[1]
                if 0 <= new_sr < len(image) and 0 <= new_sc < len(image[0]) and (new_sr, new_sc) not in visited and image[new_sr][new_sc] == image[sr][sc]:
                    visited.add((new_sr, new_sc))
                    dfs(new_sr, new_sc, visited, image)
            image[sr][sc] = newColor
        dfs(sr, sc, visited, image)
        return image
