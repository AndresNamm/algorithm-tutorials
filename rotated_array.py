
from math import floor
from sys import  maxsize

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findCount(self, A, B):
        fp = self.findFirstOccurence(A,B)
        lp = self.findLastOccurence(A,B)
        ans = lp-fp + 1 if lp > -1 else 0
        return ans

    def findMin(self, A):
        maxIndx=len(A)-1
        minIndx=0


        while minIndx<=maxIndx:
            midIndx= int((maxIndx+minIndx)/2)
            midVal=A[midIndx]
            bmidVal=A[midIndx-1] if midIndx!=0 else len(A)-1
            amidVal=A[midIndx+1] if midIndx!=len(A)-1 else 0
            if midVal<amidVal and midVal<bmidVal:
                return midVal
            elif midVal>A[maxIndx]:
                minIndx=midIndx+1
            elif midVal<A[maxIndx]:
                maxIndx=midIndx-1
        return -1

    def findFirstOccurence(self, A, num):
        maxIndx=len(A)-1
        minIndx=0
        while minIndx<=maxIndx:
            midIndx=floor((maxIndx+minIndx)/2)
            midVal=A[midIndx]
            bmidVal=A[midIndx-1] if midIndx!=0 else -1
            if midVal==num and bmidVal<midVal:
                return midIndx
            elif num<=midVal:
                maxIndx=midIndx-1
            elif num>midVal:
                minIndx=midIndx+1
        return -1



    def findLastOccurence( self,A, num):
        maxIndx=len(A)-1
        minIndx=0
        while minIndx<=maxIndx:
            midIndx=floor((maxIndx+minIndx)/2)
            midVal=A[midIndx]
            amidVal = A[midIndx + 1] if midIndx != len(A) - 1 else maxsize
            if midVal==num and amidVal>midVal:
                return midIndx
            elif num<midVal:
                maxIndx=midIndx-1
            elif num>=midVal:
                minIndx=midIndx+1
        return -1


def main():
    s = Solution()
    A=[4,5,6,7,1,2]
    res=s.findMin(A)
    print(res)

    # TEST CASE FOR SECOND SOLUTIONS
    # A=[5, 7,7, 7, 8, 8,8, 10]
    # res=s.findFirstOccurence(A,8)
    # print(res)
    #
    # res=s.findLastOccurence(A,8)
    # print(res)

if __name__ == "__main__":
    # execute only if run as a script
    main()




