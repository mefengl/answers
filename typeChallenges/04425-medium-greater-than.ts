// ============= Test Cases =============
import type { Equal, Expect } from './test-utils'

type cases = [
  Expect<Equal<GreaterThan<1, 0>, true>>,
  Expect<Equal<GreaterThan<5, 4>, true>>,
  Expect<Equal<GreaterThan<4, 5>, false>>,
  Expect<Equal<GreaterThan<0, 0>, false>>,
  Expect<Equal<GreaterThan<20, 20>, false>>,
  Expect<Equal<GreaterThan<10, 100>, false>>,
  Expect<Equal<GreaterThan<111, 11>, true>>,
]


// ============= Your Code Here =============

type GreaterThan1<T extends number, U extends number, TA extends unknown[] = [], UA extends unknown[] = []> = TA['length'] extends T
  ? false
  : UA['length'] extends U
  ? true
  : GreaterThan1<T, U, [1, ...TA], [1, ...UA]>

// TA, UA is the same array
type GreaterThan<T extends number, U extends number, A extends unknown[] = []> = A['length'] extends T
  ? false
  : A['length'] extends U
  ? true
  : GreaterThan1<T, U, [1, ...A], [1, ...A]>

// another funny idea is can TA extends [...UA, ...any] ?
// from https://github.com/type-challenges/type-challenges/issues/14098
