// ============= Test Cases =============
import type { Equal, Expect } from './test-utils'

type cases = [
  Expect<Equal<Unique<[1, 1, 2, 2, 3, 3]>, [1, 2, 3]>>,
  Expect<Equal<Unique<[1, 2, 3, 4, 4, 5, 6, 7]>, [1, 2, 3, 4, 5, 6, 7]>>,
  Expect<Equal<Unique<[1, 'a', 2, 'b', 2, 'a']>, [1, 'a', 2, 'b']>>,
  Expect<Equal<Unique<[string, number, 1, 'a', 1, string, 2, 'b', 2, number]>, [string, number, 1, 'a', 2, 'b']>>,
  Expect<Equal<Unique<[unknown, unknown, any, any, never, never]>, [unknown, any, never]>>,
]


// ============= Your Code Here =============
// can't deal with number|string|... 
type Unique1<T, U extends unknown[] = [], U2Union = U[number]> =
  T extends [infer F, ...infer R]
  ? F extends U2Union
  ? Unique1<R, U>
  : Unique1<R, [...U, F]>
  : U

// still can't, but more simple
// from https://github.com/type-challenges/type-challenges/issues/5406
type Unique2<T extends unknown[], U extends unknown[] = []> =
  T extends [infer F, ...infer R]
  ? Unique2<R, F extends U[number] ? U : [...U, F]>
  : U;

// from https://github.com/type-challenges/type-challenges/issues/14151
type Includes<T, U> = U extends [infer F, ...infer R]
  ? (<V>() => V extends F ? 0 : 1) extends (<V>() => V extends T ? 0 : 1)
    ? true
    : Includes<T, R>
  : false

type Unique<T extends unknown[], U extends unknown[] = []> =
  T extends [infer F, ...infer R]
  ? Unique<R, Includes<F, U> extends true ? U : [...U, F]>
  : U;
