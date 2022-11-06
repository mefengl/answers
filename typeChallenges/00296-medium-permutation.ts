// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

type cases = [
  Expect<Equal<Permutation<"A">, ["A"]>>,
  Expect<
    Equal<
      Permutation<"A" | "B" | "C">,
      | ["A", "B", "C"]
      | ["A", "C", "B"]
      | ["B", "A", "C"]
      | ["B", "C", "A"]
      | ["C", "A", "B"]
      | ["C", "B", "A"]
    >
  >,
  Expect<
    Equal<
      Permutation<"B" | "A" | "C">,
      | ["A", "B", "C"]
      | ["A", "C", "B"]
      | ["B", "A", "C"]
      | ["B", "C", "A"]
      | ["C", "A", "B"]
      | ["C", "B", "A"]
    >
  >,
  Expect<Equal<Permutation<boolean>, [false, true] | [true, false]>>,
  Expect<Equal<Permutation<never>, []>>
];

// ============= Your Code Here =============
type Permutation1<T> = [T] extends [never]
  ? []
  : // T will change during the traverse
  T extends infer U
  ? [U, ...Permutation1<Exclude<T, U>>]
  : [];

// https://ghaiklor.github.io/type-challenges-solutions/en/medium-permutation.html
// [T] extends [never], check https://github.com/type-challenges/type-challenges/issues/614#issue-779242337
type Permutation<T, C = T> = [T] extends [never]
  ? []
  : C extends infer U
  ? // another way is 'K extends K', also check https://github.com/type-challenges/type-challenges/issues/614#issue-779242337
    [U, ...Permutation<Exclude<T, U>>]
  : [];
