
function twoSum(nums, target) {
    table = {}
    for(let i = 0; i < nums.length; i++)  {

        val = target - nums[i]
        val_from_map = table[val]

        if(!(val in table)){
            table[nums[i]] = i
        }
        else 
            return [i, val_from_map]
    }
}


console.log(twoSum([2,7,11,15], 9))
