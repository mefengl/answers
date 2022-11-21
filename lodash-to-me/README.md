# lodash-to-me

souce code, of course, or what?

参考：

> https://underglaze-blue.github.io/lodash-analysis/start/start.html

when dealing with left or right traverse, lodash way is to have a basexxx, and then make xxx(left) and xxxright easily. And in basexxx, two direction is not make things complex at all, just takes two ternary operator(one is `fromRight ? index-- : ++index < length`)

## Array

chunk

做多栏布局的时候，划分数据

```js
/** 从 lodash 的源码中，比较醒目的是，
 *  while 替代 for 循环
 *  从下面的代码中，的确 while 比 for 代码看起来更简洁，在表达上也更自由
 */
index = 0;
while (index < length) {
  result[resIndex++] = slice(array, index, (index += size));
}
```

compact

不用写 if 判断，方便的过滤掉数组中的假值

```js
// for...of 遍历可迭代对象
// if(value)
// result[resIndex++] = value
```

concat

合并多个 flatten 的数组或值

difference

比较同一用户关注列表的变化

differenceBy

单元函数的返回值作为比较的依据

differenceWith

comparator 作为比较函数

drop

从左删除 n 个元素

dropRight

从右删除 n 个元素

dropRightWhile

从右删除满足条件的元素

dropWhile

从左删除满足条件的元素

fill

可以用于初始化数组的一部分

findIndex

自定义匹配函数

```js
// just go through a array, do not need modify the 'predicate' like findKey does
```

findLastIndex

从后往前的 findIndex

first

不用担心 IndexError 的 array[0]，LISP 的 car

flatten

只拆一层

flattenDeep

拆掉所有层

flattenDepth

指定拆层数

fromPairs

[['x', 1], ['y', 2]] => {'x': 1, 'y': 2}

head

first，不过 4 个字母

```js
const head(arr) => arr != null && arr.length ? arr[0] : undefined
// or, because arr != null is enough
const head = (arr) => arr && arr[0]
```

indexOf

```js
// traverse array in a normal way, yes, O(n), so what? now you can have your own indexOf, that's what really important
const indexOf = (arr, value) => {
  let index = -1;
  const length = arr.length;
  while (++index < length) {
    if (arr[index] === value) {
      return index;
    }
  }
  return -1;
};
```

initial

```js
const initial = (arr) => {
  let i = arr.length - 1;
  const res = new Array(i);
  while (i--) {
    res[i] = arr[i];
  }
  return res;
};
// well, basically, if you change i to end-start, then you get slice, really no magic here
```

intersection

交集

intersectionBy

交集，单元函数的返回值作为比较的依据

intersectionWith

交集，comparator 作为比较函数

join

JS 有了它的 join

last

不用担心 IndexError 的 array[-1]

```js
const last = (arr) => (arr && arr[arr.length - 1]) || undefined;
```

lastIndexOf

匹配函数是==的 findLastIndex

nth

不用担心 IndexError 的 array[n]

pull

批量删除指定元素

pullAll

pull 一个数组中 All 元素

pullAllBy

pullAll，单元函数的返回值作为比较的依据

pullAllWith

pullAll，comparator 作为比较函数

pullAt

删除索引们对应的元素

remove

删除满足条件的元素

reverse

JS 有了它的 reverse

slice

JS 有了它的切片

sortedIndex

查找插入位置

sortedIndexBy

查找插入位置，单元函数的返回值作为比较的依据

sortedIndexOf

在 sorted 数组中求 indexOf

sortedLastIndex

在 sorted 数组中求 lastIndexOf

sortedUniq

在 sorted 数组中求 uniq

sortedUniqBy

sortedUniq，单元函数的返回值作为比较的依据

tail

不用担心 IndexError 的 array[1:]，LISP 的 cdr

take

不用担心 IndexError 的 array[:n]

takeRight

不用担心 IndexError 的 array[-n:]

takeRightWhile

从右压仓

takeWhile

从左压仓

union

并集

unionBy

union，单元函数的返回值作为比较的依据

unionWith

union，comparator 作为比较函数

uniq

去重

uniqBy

uniq，单元函数的返回值作为比较的依据

uniqWith

uniq，comparator 作为比较函数

unzip

行列互换

unzipWith

unzip，提供合并函数

without

不原地修改的 pull

xor

异或

xorBy

xor，单元函数的返回值作为比较的依据

xorWith

xor，comparator 作为比较函数

zip

将参数中的数组合并成一个数组，然后行列互换

zipObject

将参数中的数组合并成一个数组，然后 fromPairs

zipObjectDeep

智能的 zipObject

zipWith

zip，提供合并函数

## Collection

countBy

计数，单元函数的返回值作为计数的依据

every

所有元素满足条件

```js
// 常见的迭代过程中return false，循环外return true的写法，做了一个封装
```

filter

不原地修改的 remove

```js
result[resIndex++] = value;
```

find

找到第一个满足 predicate 的元素

findLast

find，但最后一个

flatMap

map，然后 flatten

flatMapDeep

map，然后 flattenDeep

flatMapDepth

map，然后 flattenDepth

forEach

可以用在字典上的 forEach

forEachRight

反向遍历

groupBy

```js
// Copilot's code, thank you, Copilot
const groupBy = (array, iteratee) => {
  return array.reduce((result, value) => {
    const key = iteratee(value);
    (result[key] || (result[key] = [])).push(value);
    return result;
  }, {});
};
```

includes

是否包含

invokeMap

LISP 中的 mapcar

keyBy

提取数组中某值作为数组的 key，可以是单元函数

```js
const keyBy = (array, iteratee) => {
  return array.reduce((result, value) => {
    result[iteratee(value)] = value;
    return result;
  }, {});
};
```

map

```js
// arrayMap
const arrayMap = (array, iteratee) => {
  let i = array.length || 0;
  const result = new Array(i);
  while (i--) {
    result[i] = iteratee(array[i]);
  }
};
// baseMap, mapObject in old version Lodash
const baseMap = (object, iteratee) => {
  const result = {};
  Object.keys(object).forEach((key) => {
    result[key] = iteratee(object[key]);
  });
  return result;
};
// standard, traverse from left to right, and give iteratee three arguments
const map = (array, iteratee) => {
  let index = -1;
  const length = array.length || 0;
  const result = new Array(length);
  while (++index < length) {
    result[index] = iteratee(array[index], index, array);
  }
};
```

orderBy

sortBy，但是接受的是一一对应的函数数组和排序方向数组

partition

根据 predicate 的真假结果分成两个数组

reduce

JS 有了它的 reduce

reduceRight

reduce，但是反向

reject

类似 filter，但是假值留下

sample

单个采样

sampleSize

指定数量采样

shuffle

JS 有了它的 shuffle

size

JS 有了它的 len

some

至少有一个

sortBy

排序，单元函数的返回值作为排序依据

## Date

now

得到 timestamp

## Function

after

生成一个调用 n 次后才会执行的函数，可以用在模型训练中的 500 次循环输出一次的场景

ary

控制函数获取的参数个数，并不知道有什么用

before

生成一个调用 n 次前才会执行的函数，可以用在闹钟的贪睡功能

创建 n 的闭包，每次调用都会减少 n 的值，当 n 为 0 时，将 func 置为 undefined，将其释放，这样，之后调用的时候就不会再执行 func 了

bind

想不到使用的场景，this 的问题箭头函数可以解决

bindKey

绑定 key，key 对应的值可以更改，从而实现更改绑定的函数

curry

柯里化

curryRight

curry，但是参数右对齐

debounce

防抖，可以用在搜索框的输入

```js
// still dont't know why
// but have a short version for own purpose
const debounce = (func, wait) => {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), wait);
  };
};
```

defer

延迟执行，setTimeout(func, 1ms)

delay

defer，但是可以指定延迟时间（那和 setTimeout 有什么区别？

flip

参数反转

```js
const flip =
  (func) =>
  (...args) =>
    func(...args.reverse());
```

memoize

记忆函数，似乎是通过指针判断是否已经计算过

negate

「函数」取反

once

只承认第一次调用的参数，将函数转为单例

overArgs

参数转换，然后分配给多个函数

partial

柯里化？

partialRight

partial，但是参数右对齐

rearg

参数重排

rest

参数转换，将剩余参数转为数组

spread

参数转换，将数组转为参数

throttle

节流，可以用在滚动加载，和 debounce 的区别是，throttle 能保证每隔一段时间执行

unary

ary，但是 ary(func, 1)

wrap

给函数包装一层，不知道有什么用

## Lang

castArray

提取多个参数中的第一个，转 Array

```js
// 通用：将任意值转为数组
Array.isArray(value) ? value : [value];
```

clone

JS 有了它的 copy

cloneDeep

clone，但是深拷贝

cloneDeepWith

cloneDeep，但是可以指定拷贝规则

cloneWith

clone，但是可以指定拷贝规则

conformsTo

every，但可以方便分属性确认

```js
// lodash 直接返回结果的函数命名结尾带 To，比如该函数就有 conforms 的版本
// 再比如，内部函数有 baseConformsTo，和 baseConforms
// 参数有 source, keyToFunc，提取 source 的 key，然后用keyToFunc[key]来判断
```

eq

NaN == NaN 的比较

gt

```js
const gt = (value, other) => +value > +other;
```

gte

```js
const gte = (value, other) => +value >= +other;
```

isArguments

判断是否是 arguments 对象？

isArray

判断是否是数组

isArrayBuffer

判断是否是 ArrayBuffer

isArrayLike

判断是否是类数组，比如 HTMLCollection

isArrayLikeObject

isArrayLike，但是元素是对象

isBoolean

判断是否是 bool

isBuffer

判断是否是 Buffer

isDate

判断是否是 Date

isElement

判断是否是 DOM 元素

isEmpty

human understandable empty

isEqual

eq，但是比较内在结构

isEqualWith

isEqual，但是可以指定比较规则

isError

判断是否是 Error

isFinite

判断是否不是 Infinity

isFunction

判断是否是 function

isInteger

判断是否是 integer

isLength

判断一个数是否可能是数组的 length

isMap

判断是否是 Map

isMatch

部分 eq

isMatchWith

isMatch，但是可以指定比较规则

isNaN

判断是否是 NaN

isNative

判断是否是 native 函数

isNil

判断是否是 null 或者 undefined

isNull

判断是否是 null

isNumber

判断是否是 number，包括 NaN，Infinity

isObject

判断是否是 object

isObjectLike

isObject，但是 typeof objectLike == 'object'

isPlainObject

判断是否为一代对象

isRegExp

判断是否是 RegExp

isSafeInteger

判断是否是 IEEE-754 双精度整数

isSet

判断是否是 Set

isString

判断是否是 string

isSymbol

判断是否是 symbol

isTypedArray

判断是否是 TypedArray，比如 Uint8Array

isUndefined

判断是否是 undefined

isWeakMap

判断是否是 WeakMap

isWeakSet

判断是否是 WeakSet

lt

<

```js
const lt = (value, other) => +value < +other;
```

lte

```js
const lte = (value, other) => +value <= +other;
```

<=

toArray

是 object，就转为 array

toFinite

转为 finite

toInteger

转为 integer

toLength

转为可能的 length

toNumber

转为 number

toPlainObject

转为一代对象

toSafeInteger

转为 IEEE-754 双精度整数

toString

转为 string，其实 JS 已经有了

```js
// 转字符串
`${value}`;
// 数组转字符串
const toString = (value) => `${value.map((v) => (v == null ? v : `${v}`))}`;
// 嵌套数组转字符串
const toString = (value) => {
  if (Array.isArray(value)) {
    return `${value.map((v) => (v == null ? v : toString(v)))}`;
  } else {
    return `${value}`;
  }
};
```

## Math

add

\+

ceil

向上取整，可以指定小数点前后位数

divide

/

floor

向下取整，可以指定小数点前后位数

max

```js
// yes, O(n), also no magic here
const max = (array) => array.reduce((a, b) => (a > b ? a : b));
```

maxBy

```js
// O(2n)'s version, and simple reduce
const maxBy = (array, iteratee) =>
  array.reduce((a, b) => (iteratee(a) > iteratee(b) ? a : b));
// O(n) version
const maxBy = (array, iteratee) => {
  let result = array[0];
  let computed = iteratee(array[0]);
  // yes, calculate array[0] twice... what a waste
  array.forEach((v) => {
    const current = iteratee(v);
    if (current > computed) {
      result = v;
      computed = current;
    }
  });
};
```

mean

```js
// mean = sum / length
const mean = (array) => array.reduce((a, b) => a + b) / array.length;
// or
const mean = (array) => sum(array) / array.length;
```

meanBy

```js
const meanBy = (array, iteratee) =>
  array.reduce((a, b) => a + iteratee(b)) / array.length;
// or
const meanBy = (array, iteratee) => sumBy(array, iteratee) / array.length;
```

min

JS 有了它的 min

minBy

min，但是可以指定映射方式

multiply

\*

round

四舍五入，可以指定小数点前后位数

subtract

\-

sum

```js
const sum = (array) => array.reduce((a, b) => a + b);
// or baseSum(array, v => v)
const baseSum = (array, iteratee) => array.reduce((a, b) => a + iteratee(b), 0);
const sum = (array) => baseSum(array, (v) => v);
```

sumBy

```js
// just baseSum
const sumBy = (array, iteratee) => baseSum(array, iteratee);
// const baseSum = (array, iteratee) => array.reduce((a, b) => a + iteratee(b), 0);
```

## Number

clamp

toSafeInteger，但是可以指定上下限

```js
// 问：一个三元表达式，可以实现上界或下界，如何实现上下界？
// 答：两个三元表达式
num = num > max ? max : num;
num = num < min ? min : num;
```

inRange

```js
const inRange = (num, start, end) => num >= start && num < end;
// a complex version
// a public code package's problem is too much consideration for all situation.
// but we don't have to consider that much to write our own 'inRange' or many other more common function
const baseInRange = (num, start, end) => {
  return num >= Math.min(start, end) && num < Math.max(start, end);
};
const inRange = (num, start, end) => {
  if (end === undefined) {
    end = start;
    start = 0;
  }
  return baseInRange(num, start, end);
};
```

random

JS 有了它的 random， random(int)是 randint， random(int, int)是 randrange， random(int, true)是 randfloat

## Object

assign

\*不知道有什么用

assignIn

\*assign，但是会把原型链上的属性也拷贝

assignInWith

\*assignIn，但是可以指定拷贝规则

assignWith

\*assign，但是可以指定拷贝规则

at

\*通过 path 数组获取对象的值

用`...paths`接受参数，利用 baseFlatten 把剩余参数展开一层，这样数组参数和非数组参数就可以同样处理了

eg:

```js
var object = { a: [{ b: { c: 3 } }, 4] };

at(object, ["a[0].b.c", "a[1]"]); // [3, 4]
at(object, "a[0].b.c", "a[1]"); // [3, 4]

/** from https://underglaze-blue.github.io/lodash-analysis/export/at.html */
```

create

\*指定继承属性

defaults

批量指定候选默认值，defaultToAny 是指定批量候选默认值

```js
function defaults(object, ...source) {
  source.forEach((s) => {
    for (const key in s) {
      if (object[key] === undefined) {
        object[key] = s[key];
      }
    }
  });
  return object;
}
```

defaultsDeep

defaults，但是不止一层

findKey

find，但是返回 key

```js
// key相关，有value=object[key]
// 遍历相关，类似map，不过最后返回undefined
```

findLastKey

findKey，但是从后往前

```js
// by something we called 'baseXXX', and with traverse tricks in it, can easily implement both 'xxx' and 'xxxLast'
```

forIn

可以用在字典上的 forIn

forInRight

forIn，但是从后往前

forOwn

\*遍历定义时的属性

```js
// traverse object
Object.keys(object).map((key) => xxx);
// or
Object.entries(object).map(([key, value]) => xxx);
```

forOwnRight

```js
// forOwn(xxx)'s keypoint is Object.keys(object), not forEach, forEach is just a grammar sugar to traverse `keys`
const props = Object.keys(object);
let length = props.length;
while (length--) {
  const key = props[length];
  object[key];
}
```

functions

forOwn，但是 only 返回函数属性的名字

```js
// the way to get some specific properties of an object
Object.keys(obj).filter((key) => typeof object[key] === "specific type");
```

functionsIn

functions，但是非定义时的函数属性的名字也会返回

get

```js
// the way to get a deep property of an object
const path = "ui.color.red".split(".");
// or
const path = ["ui", "color", "red"];
let i = 0;
const len = path.length;
// if use obj && xxx, "" will be treated as false, that is not what we want
while (obj != null && i < len) {
  obj = obj[path[i++]];
}
```

has

at，但是只判断是否存在

hasIn

has，但是会检查原型链上的属性

invert

```js
const invert(object) {
  const result = {};
  Object.keys(object).forEach((key) => {
    // should check if value is false, but "",undefined,null,0,false won't get error, they are valid key value
    const value = object[key];
    objcet[value] = key;
    // result[object[key]] = key;
  });
  return result;
}
```

invertBy

invert，但是可以指定 values_to_key 的映射方式

invoke

```js
const invoke = (object, path, ...args) => {
  // get = toPath + while loop logic
  path = Array.isArray(path) ? path : path.split(".");
  const length = path.length;
  let i = -1;
  while (++i < length) {
    object = object[path[i]];
  }
  const func = object;
  return func(...args);
};
```

keys

```js
for (const key in object) {
  if (object.hasOwnProperty(key)) {
    keys.push(key);
  }
}
// or
Object.keys(object);
```

keysIn

```js
// also keys in prototype chain, I don't know, haven't met similar use case before
for (const key in object) {
  keys.push(key);
}
```

mapKeys

map，但是只映射 key

```js
const mapKeys = (object, iteratee) => {
  const result = {};
  Object.keys(object).forEach((key) => {
    // iteratee always take value, key, object in lodash
    // with value is cool, you can change key depend on value
    // here we only take the key
    const newKey = iteratee(key);
    result[newKey] = object[key];
    // result[iteratee(object[key])] = object[key];
  });
  return result;
};
```

mapValues

```js
const mapValues = (object, iteratee) => {
  const result = {};
  Object.keys(object).forEach((key) => {
    const newValue = iteratee(object[key]);
    result[key] = newValue;
    // result[key] = iteratee(object[key]);
  });
  return result;
};
```

merge

```js
// too complex, can't understand, yet
```

mergeWith

merge，但是可以指定合并规则

omit

不要指定的属性，和 pick 相反

omitBy

omit，但是可以指定过滤方式，比如\_.isNumber

pick

只要指定的属性，和 omit 相反

pickBy

pick，但是可以指定过滤方式，比如\_.isNumber

result

\*get，但可以调用函数

set

指定路径赋值

setWith

set，但是可以指定赋值规则

toPairs

键值对转为数组

toPairsIn

toPairs，但是会检查原型链上的属性

transform

\*reduce 的替代

unset

指定路径恢复出厂设置

update

set，但是可以指定 updater

updateWith

setWith，但是可以指定 updater

values

返回字典的 value 数组

valuesIn

values，但是会检查原型链上的属性

## Seq

\_

类似 jQuery 的$，转化后就可以链式调用

chain

\_，但是需要调用 value 取值

tap

\*tap into

thru

\*pass thru

prototype[Symbol.iterator]

\*I don't know

prototype.at

\*wrapper version of \_.at

prototype.chain

\*wrapper version of \_.chain

prototype.commit

执行链式调用

prototype.next

\*返回下一个值

prototype.plant

\*同 chain，但是新的初始值

prototype.reverse

\*wrapeer version of \_.reverse

prototype.value

返回解析值

## String

camelCase

驼峰命名

```js
// 通用：通过参数传递调用方法
value[methodName](...args); // 就像是字典 .name 和 ["name"] 一样
// 「一个方法就是一个可以被调用的属性而已」 from @Underglaze-Blue

/** 类似驼峰命名这样的函数，可以抽象为对字符串某个「特殊位置」的「特殊处理」
 * 特殊处理可以是 首字母大写 ，特殊位置可以是 string[0]
 * 比如lodash就专门封装了一个函数工厂createCaseFirst，返回对「首字母」进行由参数指定的「特殊处理」的函数
 * 即：const upperFirst = createCaseFirst('toUpperCase')
 * 太优雅了
 */

// 通用：跳过 index 为0的情况
index ? callFunction : notCallFunction;
```

capitalize

首字母大写

```js
upperFirst(string.toLowerCase());
```

deburr

去除重音符号

endsWith

是否以指定字符串结尾

```js
string.slice(posion, end) === target;
```

escape

为 HTML 转义

escapeRegExp

为正则表达式转义

kebabCase

短横线命名

lowerCase

小写命名

lowerFirst

首字母小写

pad

左右填充至指定长度

padEnd

右填充至指定长度

padStart

左填充至指定长度

parseInt

转成整数

repeat

重复指定次数

replace

替换

snakeCase

下划线命名

split

分割

startCase

首字母大写命名

startsWith

是否以指定字符串开头

template

\*有了模版字符串，这个就没啥用了

toLower

全小写

toUpper

全大写

trim

去除首尾填充

trimEnd

去除尾部填充

trimStart

去除首部填充

truncate

限制字符串长度，自动添加省略号「...」，可以用在标题上

unescape

反 escape

upperCase

全大写命名

upperFirst

首字母大写

words

分割成单词

```js
// lodash 的做法是利用正则表达式提取出所有单词，很反逻辑，不过这样就可以自己决定哪些是单词了
// 日常 空格分割 还是 .split(' ')
```

## Util

attempt

不用 catch 的 try，可以用在 querySelector，但似乎 jQuery 已经有了

bindAll

绑定对象的方法们到对象上

cond

类似 switch ，但条件是函数，返回是函数（可以很方便的复用）

```js
pairs = [
  [condition, action],
  [condition, action],
  ...
];

function cond(pairs) {
  return function (value) {
for (const [condition, action] of pairs) {
  if (condition(value)) {
    return action(value);
  };
}
  }
}
```

conforms

类似\_.matches，但条件是函数

constant

\*将值转为函数

defaultTo

`value = value == null ? defaultValue : value`
and deal with NaN
`value = value !== value ? defaultValue : value`

defaultToAny

类似 defaultTo，但可以传多个值，返回第一个不是 null 或 undefined 的值

`defaultToAny(a,b,c,d) = [a,b,c,d].reduce(defaultTo)`

`defaultToAny(a,b,c,d) = defaultTo(defaultTo(defaultTo(a, b),c),d)`

flow

compose 格式的 chain，或者说 reversed compose

```js
const flow = (...fs) => {
  const length = fs.length
  return (...args) => {
    let index = -1
    let result = ...args
    while (++index < length) {
      // don't know why there need to use call(this,result)
      result = fs[index](result)
    }
    return result
  }
}
```

flowRight

compose，但接受函数数组，而不是多个函数参数

```js
const flowRight = (...fs) => flow(...fs.reverse())
// or
const flowRight = (fs) => {
  let length = fs.length
  return (...args) => {
    let result = ...args
    while (length--) {
      result = fs[index](result)
    }
    return result
  }
}
```

identity

返回第一个参数

iteratee

\*按某种自定义的规则提取数组

matches

```js
// it's job is to return a function that can use in filter or sth. like that
// by far, I only understand the getMatchData part, kind of like entries
const getMatchData = (object) => {
  const props = Object.keys(object);
  let i = props.length;
  const result = new Array(i);
  while (i--) {
    const key = props[i];
    const value = object[key];
    result[i] = [key, value];
    // result[i] = [props[i], object[props[i]]];
  }
};
```

matchesProperty

创建一个函数，判断对象的指定属性是否符合条件，可以用于*.filter，*.find

method

```js
const method = (path, ...args) => {
  // toPath function
  path = Array.isArray(path) ? path : path.split(".");
  const length = path.length;
  return (object) => {
    let index = -1;
    // get function
    while (++index < length) {
      object = object[path[index]];
    }
    const func = object;
    return func(...args);
  };
};
// or
const method = (path, ...args) => {
  // because the toPath is implemented in a idempotent way, it ok that translate path to array here
  return (object) => invoke(object, path, ...args);
```

methodOf

```js
// basically the same as method, in code level
const methodOf = (object, ...args) => {
  return (path) => {
    // toPath function
    path = Array.isArray(path) ? path : path.split(".");
    const length = path.length;
    let index = -1;
    while (++index < length) {
      object = object[path[index]];
    }
    const func = object;
    return func(...args);
  };
};
// or
const methodOf = (object, ...args) => {
  return (path) => invoke(object, path, ...args);
};
```

mixin

给对象添加方法，可以用于扩展 lodash

noConflict

恢复\_的原始值

noop

undefined 制造机

nthArg

返回第 n 个参数的函数

over

批量执行函数，返回结果数组

overEvery

over + every

overSome

over + some

property

有 path，等待 object 去取值的函数

propertyOf

有 object，等待 path 去取值的函数

range

JS 有了它的 range

rangeRight

JS 有了它的 reversed(range)

runInContext

\*创建一个新的 lodash 实例

stubArray

[]

stubFalse

false

stubObject

{}

stubString

""

stubTrue

true

times

执行 n 次，比如结合 stubArray，创建 n 个空数组

toPath

从字符串 path 转成 path 数组

```js
const toPath = (string) => {
  return string.split(".");
  // idempotent version
  // return isArray(value) ? string : string.split('.');
};
```

uniqueId

添加唯一 id

## Properties

\*I don't know

## Methods

\*I don't know

## Internal

baseWhile

```js
functioni baseWhile(array, predicate, isDrop, fromRight){
  const { length } = array;
  // 和下面的while条件配合，可以通过一个变量控制循环方向
  let index = fromRight ? length : -1;
  while (
    (fromRight ? index-- : ++index < length) &&
    predicate(array[index], index, array)
  ) {}
  // 两个值的三元运算符，四种情况，一行
  return isDrop
    ? slice(array, fromRight ? 0 : index, fromRight ? index + 1 : length)
    : slice(array, fromRight ? index + 1 : 0, fromRight ? length : index);
}
```

baseFlatten

```js
function baseFlatten(array, depth, result) {
  for (const value of array) {
    // !Array.isArrary(value) is one of the base cases of recursion
    // so flattenDeep is just flatten with depth = Infinity
    // Infinity = 1/0 by the way
    if (depth > 0 && Array.isArray(value)) {
      if (depth > 1) {
        baseFlatten(value, depth - 1, result);
      } else {
        result.push(...value);
      }
    } else {
      result[result.length] = value;
    }
  }
  return result;
}
```

## Old Version Methods

getTag

```js
// it's ok to create a grammar sugar for oneself, such as
const toString = Object.prototype.toString;
const getTag = (value) => toString(value);
// standard
const getTag = (value) => {
  if (value == null) {
    return value === undefined ? "[object Undefined]" : "[object Null]";
  }
  return toString(value);
};
```
