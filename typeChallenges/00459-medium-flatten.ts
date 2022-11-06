// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

type cases = [
  Expect<Equal<Flatten<[]>, []>>,
  Expect<Equal<Flatten<[1, 2, 3, 4]>, [1, 2, 3, 4]>>,
  Expect<Equal<Flatten<[1, [2]]>, [1, 2]>>,
  Expect<Equal<Flatten<[1, 2, [3, 4], [[[5]]]]>, [1, 2, 3, 4, 5]>>,
  Expect<
    Equal<
      Flatten<[{ foo: "bar"; 2: 10 }, "foobar"]>,
      [{ foo: "bar"; 2: 10 }, "foobar"]
    >
  >
];

// ============= Your Code Here =============
// base case
type Flatten1<T> = T extends [] ? [] : T;

type Flatten<T> = T extends []
  ? []
  : T extends [infer H, ...infer R]
  ? // if is an array
    // R is exactly the T cut the head off
    // so Flatten<R> just another Flatten<T>
    // Flatten<H> => [H] / []
    // ... really do the jobs, like [H] => H
    [...Flatten<H>, ...Flatten<R>]
  : // if is value
    [T];
