// ============= Test Cases =============
import type { Equal, Expect } from './test-utils'

const promiseAllTest1 = PromiseAll([1, 2, 3] as const)
const promiseAllTest2 = PromiseAll([1, 2, Promise.resolve(3)] as const)
const promiseAllTest3 = PromiseAll([1, 2, Promise.resolve(3)])

type cases = [
  Expect<Equal<typeof promiseAllTest1, Promise<[1, 2, 3]>>>,
  Expect<Equal<typeof promiseAllTest2, Promise<[1, 2, number]>>>,
  Expect<Equal<typeof promiseAllTest3, Promise<[number, number, number]>>>,
]


// ============= Your Code Here =============
// declare function PromiseAll<T>(values: T): Promise<T>;

// declare function PromiseAll<T extends unknown[]>(
//   values: readonly [...T]
// ): Promise<T extends Promise<infer R> ? R : T>;

declare function PromiseAll<T extends unknown[]>(
  value: readonly [...T]
//ZZTODO: how does keyof work?
): Promise<{ [P in keyof T]: T[P] extends Promise<infer R> ? R : T[P] }>;
