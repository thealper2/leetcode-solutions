var createCounter = function(init) {
    var count = init;
    return {
        increment: () => {
            return ++count;
        },
        decrement: () => {
            return --count;
        },
        reset: () => {
            count = init;
            return count;
        }
    }
};
