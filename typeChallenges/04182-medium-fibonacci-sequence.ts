// ============= Test Cases =============
import type { Equal, Expect } from './test-utils';

type cases = [
  Expect<Equal<Fibonacci<1>, 1>>,
  Expect<Equal<Fibonacci<2>, 1>>,
  Expect<Equal<Fibonacci<3>, 2>>,
  Expect<Equal<Fibonacci<8>, 21>>,
]


// ============= Your Code Here =============

// https://github.com/type-challenges/type-challenges/issues/14095 , add some step comments and better naming

// 1: Cur = default value = [1]
// 2: Cur = Last Pre = [1]
// 3: Cur = Last Pre = [...[1], ...[1]] = [1,1]
// 4: Cur = Last Pre = [...[1,1], ...[1]] = [1,1,1]
// Cur is the Last Pre
type Fibonacci<T extends number, N extends unknown[] = [1], Cur extends unknown[] = [1], Pre extends unknown[] = [1]> =
  N['length'] extends T
  ? Cur['length']
  : Fibonacci<T, [...N, 1], Pre, [...Pre, ...Cur]>
