// ============= Test Cases =============
import type { Equal, Expect } from './test-utils'

type cases = [
  Expect<Equal<MyExclude<'a' | 'b' | 'c', 'a'>, 'b' | 'c'>>,
  Expect<Equal<MyExclude<'a' | 'b' | 'c', 'a' | 'b'>, 'c'>>,
  Expect<Equal<MyExclude<string | number | (() => void), Function>, string | number>>,
]


// ============= Your Code Here =============
// extends can be used in two ways
// one is a real extends
// another is a question with the traverse of T, called Distributive Conditional Types
// second one can be used in a fun way, like Flatten
// type Flatten<T> = T extends any[] ? T [number]: T;
type MyExclude<T, U> = T extends U ? never : T
// https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#distributive-conditional-types
