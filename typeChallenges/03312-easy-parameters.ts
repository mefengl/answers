// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

const foo = (arg1: string, arg2: number): void => {};
const bar = (arg1: boolean, arg2: { a: "A" }): void => {};
const baz = (): void => {};

type cases = [
  Expect<Equal<MyParameters<typeof foo>, [string, number]>>,
  Expect<Equal<MyParameters<typeof bar>, [boolean, { a: "A" }]>>,
  Expect<Equal<MyParameters<typeof baz>, []>>
];

// ============= Your Code Here =============
// https://ghaiklor.github.io/type-challenges-solutions/en/easy-parameters.html
// in the above link, the way to get the answer is elegant
type MyParameters<T extends (...args: any[]) => any> = T extends (
  ...args: infer P
) => any
  ? P
  : never;
