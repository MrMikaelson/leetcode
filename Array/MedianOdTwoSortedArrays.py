class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = 0
        n = 0
        merge = []
        while m<len(nums1) and n<len(nums2):
            if nums1[m] <= nums2[n]:
                merge.append(nums1[m])
                m+=1
            else:
                merge.append(nums2[n])
                n+=1
        if m < len(nums1):
            for i in range(m,len(nums1)):
                merge.append(nums1[i])
        if n < len(nums2):
            for i in range(n,len(nums2)):
                merge.append(nums2[i])
        # print(merge)
        if (len(nums1)+len(nums2))%2 != 0:
            # print(merge[(len(nums1)+len(nums2))//2])
            return float(merge[(len(nums1)+len(nums2))//2])
        else:
            # print((merge[(len(nums1)+len(nums2))//2] + merge[(len(nums1)+len(nums2))//2 - 1])/2)
            return float((merge[(len(nums1)+len(nums2))//2] + merge[(len(nums1)+len(nums2))//2 - 1])/2)