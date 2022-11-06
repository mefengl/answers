// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

type cases = [
  Expect<Equal<IsUnion<string>, false>>,
  Expect<Equal<IsUnion<string | number>, true>>,
  Expect<Equal<IsUnion<"a" | "b" | "c" | "d">, true>>,
  Expect<Equal<IsUnion<undefined | null | void | "">, true>>,
  Expect<Equal<IsUnion<{ a: string } | { a: number }>, true>>,
  Expect<Equal<IsUnion<{ a: string | number }>, false>>,
  Expect<Equal<IsUnion<[string | number]>, false>>,
  // Cases where T resolves to a non-union type.
  Expect<Equal<IsUnion<string | never>, false>>,
  Expect<Equal<IsUnion<string | unknown>, false>>,
  Expect<Equal<IsUnion<string | any>, false>>,
  Expect<Equal<IsUnion<string | "a">, false>>,
  Expect<Equal<IsUnion<never>, false>>
];

// ============= Your Code Here =============
// check T is changed after distribute
type IsUnion1<T, C = T> = T extends T
  ? // use tuple avoid type distribute, from https://github.com/type-challenges/type-challenges/issues/1227#issuecomment-824176815
    [C] extends [T]
    ? false
    : true
  : never;

// add IsNever check
type IsUnion<T, C = T> = [T] extends [never]
  ? false
  : T extends C
  ? [C] extends [T]
    ? false
    : true
  : never;
