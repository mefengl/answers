// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

type X = Promise<string>;
type Y = Promise<{ field: number }>;
type Z = Promise<Promise<string | number>>;
type Z1 = Promise<Promise<Promise<string | boolean>>>;

type cases = [
  Expect<Equal<MyAwaited<X>, string>>,
  Expect<Equal<MyAwaited<Y>, { field: number }>>,
  Expect<Equal<MyAwaited<Z>, string | number>>,
  Expect<Equal<MyAwaited<Z1>, string | boolean>>
];

// @ts-expect-error
type error = MyAwaited<number>;

// ============= Your Code Here =============
// main point is the 'infer' keyword, known as Inferring Within Conditional Types
// https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#inferring-within-conditional-types
// simple version
// type MyAwaited<T> = T extends Promise<infer R> ? MyAwaited<R> : R;
// full version
type MyAwaited<T extends Promise<unknown>> = T extends Promise<infer R>
  ? R extends Promise<unknown>
    ? MyAwaited<R>
    : R
  : never;
