var join = function(arr1, arr2) {
    const result = arr1.concat(arr2).reduce((acc, obj) => {
        acc[obj.id] = { ...acc[obj.id], ...obj };
        return acc;
    }, {});

    return Object.values(result);
};
