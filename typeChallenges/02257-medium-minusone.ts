// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

type cases = [
  Expect<Equal<MinusOne<1>, 0>>,
  Expect<Equal<MinusOne<55>, 54>>,
  Expect<Equal<MinusOne<3>, 2>>,
  Expect<Equal<MinusOne<100>, 99>>,
  Expect<Equal<MinusOne<1101>, 1100>>,
  Expect<Equal<MinusOne<0>, -1>>
];

// ============= Your Code Here =============
// can't pass `Expect<Equal<MinusOne<1101>, 1100>>`
type Tuple1<N extends number, T extends unknown[] = []> = T["length"] extends N
  ? T
  : Tuple1<N, [unknown, ...T]>;

// `0 extends 1? never : ...` is for `tail recursion`, from https://github.com/type-challenges/type-challenges/issues/18456#issue-1432554106
// also see https://devblogs.microsoft.com/typescript/announcing-typescript-4-5-beta/#tailrec-conditional
type Tuple<N extends number, T extends unknown[] = []> = 0 extends 1
  ? never
  : T["length"] extends N
  ? T
  : Tuple<N, [unknown, ...T]>;

type MinusOne<T extends number> = Tuple<T> extends [unknown, ...infer R]
  ? R["length"]
  : -1;
