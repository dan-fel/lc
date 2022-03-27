
function twoSum(nums, target) {
    table = {}
    for(let i = 0; i < nums.length; i++)  {

        val = target - nums[i]
        change_all_these_variables = table[val]

        if(!(val in table)){
            table[nums[i]] = i
        }
        else 
            return [i, change_all_these_variables]
    }
}

console.log(twoSum([2,7,11,15], 9))
