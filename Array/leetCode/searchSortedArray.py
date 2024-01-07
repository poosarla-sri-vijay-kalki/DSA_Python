def search( nums, target):
    l,r = 0, len(nums)-1
    while l<=r:
        m = (l+r)//2
        if(nums[l] == nums[m] == nums[r]):
            l+=1
            r-=1
            continue
        if(nums[m] == target):
            return True
        if nums[l] <= nums[m]:
            if(nums[l]<=target and target<nums[m]):
                r = m-1
            else:
                l=m+1
        else:
            if(nums[m]<target and target<=nums[r]):
                l = m+1
            else:
                r = m-1
    return False
     
nums = [1,0,1,1,1]
target = 0
print(search(nums, target))