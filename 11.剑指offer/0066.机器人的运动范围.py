题目描述
    地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），
因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？


核心思路：
    1.从(0,0)开始走，每成功走一步标记当前位置为true,然后从当前位置往四个方向探索，返回1 + 4 个方向的探索值之和。
    2.探索时，判断当前节点是否可达的标准为：
        1）当前节点在矩阵内；
        2）当前节点未被访问过；
        3）当前节点满足limit限制。
        
        
成功方案：
class Solution:
 
    def __init__(self):
        self.vis = {}
         
    def movingCount(self, threshold, rows, cols):
        # write code here
        return self.moving(threshold, rows, cols, 0, 0)
         
    def moving(self, threshold, rows, cols, row, col):
        if row/10 + row%10 + col/10 + col%10 > threshold:
            return 0
        if row >= rows or col >= cols or row < 0 or col < 0:
            return 0
        if (row, col) in self.vis:
            return 0
        self.vis[(row, col)] = 1
         
        return 1 + self.moving(threshold, rows, cols, row-1, col) + self.moving(threshold, rows, cols, row+1, col) + self.moving(threshold, rows, cols, row, col-1) + self.moving(threshold, rows, cols, row, col+1)


2.class Solution:
    def __init__(self):
        self.vis=[]
    def movingCount(self, threshold, rows, cols):
        # write code here
        return self.moving(threshold,rows,cols,0,0)
    
    def moving(self,threshold,rows,cols,i,j):#i,j标记当前位置
        if i>=rows or j>=cols or i<0 or j<0:    #注意>= 而不是> 因为是从（0,0）位置开始的
            return 0
        if (i,j) in self.vis:
            return 0
        if i%10+i/10+j%10+j/10>threshold:       #注意python2  /即保留整数部分  python3  //保留整数部分  /同样保留小数部分
            return 0
        self.vis.append((i,j))                  #append（） 说明当前位置符合要求  所以最后return时要+1
        return 1+ self.moving(threshold,rows,cols,i-1,j)+self.moving(threshold,rows,cols,i+1,j)+self.moving(threshold,rows,cols,i,j-1)+self.moving(threshold,rows,cols,i,j+1)
    
    
