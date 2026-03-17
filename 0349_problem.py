# 349. Intersection of Two Arrays

def intersection(nums1,nums2):
    # l1=[]
    # for i in nums1:
    #     for j in nums2:
    #         if i==j and i not in l1:
    #             l1.append(i)

    # return l1

    return list(set(nums1) & set(nums2))




print(intersection([1,2,2,1],[1,2]))