var promiseAll = async function(functions) {
    try {
        return await Promise.all(functions.map(fn => fn()));
    } catch (error) {
        throw error;
    }
};
