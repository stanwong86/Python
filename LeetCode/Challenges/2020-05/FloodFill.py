class Solution:
    def process(self, row, col):
        self.image[row][col] = self.newColor
        
        for (x, y) in [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]:
            if 0 <= x < len(self.image) and 0 <= y < len(self.image[0]) and self.image[x][y] == self.oldColor:
                self.process(x, y)
        
    def floodFill(self, image, sr, sc, newColor):
        self.image = image
        self.oldColor = image[sr][sc]
        self.newColor = newColor
        if self.oldColor != self.newColor:
            self.process(sr, sc)
        return self.image

s = Solution()
r = s.floodFill([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], 2, 2, 1)
print(r)