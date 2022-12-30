const deepMerge = (obj1, obj2) => {
  const result = { ...obj1 };
  Object.keys(obj2).forEach(key => {
    result[key] = obj2[key] instanceof Object
      ? Array.isArray(obj2[key])
        ? [...obj1[key], ...obj2[key]]
        : deepMerge(obj1[key], obj2[key])
      : obj2[key];
  });
  return result;
};
