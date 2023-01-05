const deepMerge = (obj1, obj2) => {
  const result = { ...obj1 };
  Object.keys(obj2).forEach(key => {
    result[key] =
      (obj1[key] && obj1[key] instanceof Object && !(obj1[key] instanceof Array))
        ? deepMerge(obj1[key], obj2[key])
        : obj2[key];
  });
  return result;
};
