# MDN to me

## Function

apply

\*apply 就是 map，是一种映射方式
func.apply(null,arr) = arr.map(func)

## Object

entries

```js
Object.keys(object).map((key) => [key, obj[key]]);
// or
// ownProps because it only returns the keys of the object itself, not the keys of the prototype chain
const ownProps = Object.keys(obj);
let i = ownProps.length;
const res = new Array(i);
while (i--) {
  res[i] = [ownProps[i], obj[ownProps[i]]];
}
/* from MDN Polyfill */
```

fromEntries

```js
const res = {};
let i = arr.length;
while (i--) {
  res[arr[i][0]] = arr[i][1];
}
// or
const res = {};
arr.forEach(([key, value]) => {
  res[key] = value;
});
// or
const res = arr.reduce((acc, [key, value]) => {
  acc[key] = value;
  return acc;
}, {});
```
