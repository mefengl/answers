// ============= Test Cases =============
import type { Equal, Expect } from './test-utils'

type cases = [
  Expect<Equal<LastIndexOf<[1, 2, 3, 2, 1], 2>, 3>>,
  Expect<Equal<LastIndexOf<[2, 6, 3, 8, 4, 1, 7, 3, 9], 3>, 7>>,
  Expect<Equal<LastIndexOf<[0, 0, 0], 2>, -1>>,
  Expect<Equal<LastIndexOf<[string, 2, number, 'a', number, 1], number>, 4>>,
  Expect<Equal<LastIndexOf<[string, any, 1, number, 'a', any, 1], any>, 5>>,
]


// ============= Your Code Here =============
// count rest's length by myself...
type LastIndexOf1<
  T, U,
  Flag extends boolean = false,
  Count extends 42[] = []
> = T extends [...infer L, infer R]
  ? Flag extends true
    ? LastIndexOf1<L, U, true, [...Count, 42]>
    : (<V>() => V extends R ? 0 : 1) extends (<V>() => V extends U ? 0 : 1)
      ? LastIndexOf1<L, U, true>
      : LastIndexOf1<L, U>
  : Flag extends false
    ? -1
    : Count['length']

// by Rest['length']...
type LastIndexOf<T, U> = T extends [...infer L, infer R]
  ? (<V>() => V extends R ? 0 : 1) extends (<V>() => V extends U ? 0 : 1)
    ? L['length']
    : LastIndexOf<L, U>
  : -1
