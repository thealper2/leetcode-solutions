var cancellable = function(fn, args, t) {
    fn(...args);
    const intervalID  = setInterval(fn, t, ...args);
    return () => clearInterval(intervalID);
};
