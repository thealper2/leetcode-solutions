var once = function(fn) {
    var c = false
    return function(...args) {
        if (!c) {
            c = true;
            return fn(...args);
        }
        undefined;
    }
};
