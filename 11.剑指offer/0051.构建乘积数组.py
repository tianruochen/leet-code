题目描述
  给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
  
  
成功解法：
class Solution:
    def multiply(self, A):
        # write code here
            
        B=A[:]
        for m in range(len(A)):
            res=1
            
            for n in range(len(A)):
                if n!=m:
                    res=res*A[n]
            B[m]=res
        return B
