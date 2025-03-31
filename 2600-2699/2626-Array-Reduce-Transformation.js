var reduce = function(nums, fn, init) {
    var acc = init;
    for (var i = 0; i < nums.length; i++) {
        acc = fn(acc, nums[i]);
    }
    return acc;
};
