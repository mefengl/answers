// ============= Test Cases =============
import type { Equal, Expect } from './test-utils'

type cases = [
  Expect<Equal<IndexOf<[1, 2, 3], 2>, 1>>,
  Expect<Equal<IndexOf<[2, 6, 3, 8, 4, 1, 7, 3, 9], 3>, 2>>,
  Expect<Equal<IndexOf<[0, 0, 0], 2>, -1>>,
  Expect<Equal<IndexOf<[string, 1, number, 'a'], number>, 2>>,
  Expect<Equal<IndexOf<[string, 1, number, 'a', any], any>, 4>>,
  Expect<Equal<IndexOf<[string, 'a'], 'a'>, 1>>,
  Expect<Equal<IndexOf<[any, 1], 1>, 1>>,
]


// ============= Your Code Here =============
type MyEqual<F, U> = (<V>() => V extends F ? 0 : 1) extends (<V>() => V extends U ? 0 : 1) ? true : false
// 42[] is a array of 42, just so funny to use it
type IndexOf1<T, U, Count extends 42[] = []> =
  T extends [infer F, ...infer R] ?
  MyEqual<F, U> extends true
  ? Count['length']
  : IndexOf1<R, U, [...Count, 42]>
  : -1

type IndexOf<T, U, Count extends 42[] = []> =
  T extends [infer F, ...infer R] ?
  (<V>() => V extends F ? 0 : 1) extends (<V>() => V extends U ? 0 : 1)
  ? Count['length']
  : IndexOf<R, U, [...Count, 42]>
  : -1
