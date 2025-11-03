/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    if (!Array.isArray(arr)) {
        return;
    }
    
    for (const element of arr) {
        if (Array.isArray(element)) {
            yield* inorderTraversal(element);
        } else if (typeof element === 'number') {
            yield element;
        }
    }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */
