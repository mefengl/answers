const debounce = (func, wait) => {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), wait);
  };
};

const f = debounce(() => console.log("hello"), 200);

const start = +new Date();
while (+new Date() - start < 3000) {
  console.log("waiting...");
  f();
}
