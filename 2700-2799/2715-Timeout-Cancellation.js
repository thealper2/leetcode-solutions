var cancellable = function(fn, args, t) {
    let timerID = setTimeout(fn, t, ...args);
    return function () {
        clearTimeout(timerID);
    };
};
