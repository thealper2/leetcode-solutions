var map = function(arr, fn) {
    var arr2 = [];
    for (var i = 0; i < arr.length; i++) {
        arr2.push(fn(arr[i], i));
    }
    return arr2;
};
