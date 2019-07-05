# https://www.interviewbit.com/problems/find-duplicate-in-array/
from math import floor

class Solution:
    # @param A : tuple of integers
    # @return an integer


    def get_bucket_index(self, val, max_val, k):
        bucket_index = floor(val / (max_val + 1) * k)
        return bucket_index

    def calculate_bucket_elements(self, bucket_index, max_val, k):
        bucket_max_val=floor(((max_val+1)/k)*(bucket_index+1))
        bucket_min_val=floor(((max_val+1)/k) * bucket_index)
        bucket_vals = [i for i in range(bucket_min_val,bucket_max_val)]
        return bucket_vals

    def repeatedNumber(self, A):

        sqrt_len = int(len(A)**0.5)
        buckets = [0 for i in range(sqrt_len)]
        max_val = len(A)-1
        for val in A:
            buckets[self.get_bucket_index(val,max_val,buckets)]+=1
        #buckets=sorted(buckets, key=lambda x: x[1])
        bucket_max_allowed_size=floor(max_val/sqrt_len)

        large_buckets=[]
        for idx,count in enumerate(buckets):
            if count>bucket_max_allowed_size:
                large_buckets.append(idx)


















