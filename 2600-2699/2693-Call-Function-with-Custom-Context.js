/**
 * @param {Object} context
 * @param {Array} args
 * @return {null|boolean|number|string|Array|Object}
 */
Function.prototype.callPolyfill = function(context, ...args) {
    const uniqueKey = Symbol('tempFn');
    context[uniqueKey] = this;
    const result = context[uniqueKey](...args);
    delete context[uniqueKey];
    return result;
}

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */
