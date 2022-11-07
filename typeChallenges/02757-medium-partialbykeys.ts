// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

interface User {
  name: string;
  age: number;
  address: string;
}

interface UserPartialName {
  name?: string;
  age: number;
  address: string;
}

interface UserPartialNameAndAge {
  name?: string;
  age?: number;
  address: string;
}

type cases = [
  Expect<Equal<PartialByKeys<User, "name">, UserPartialName>>,
  Expect<Equal<PartialByKeys<User, "name" | "unknown">, UserPartialName>>,
  Expect<Equal<PartialByKeys<User, "name" | "age">, UserPartialNameAndAge>>,
  Expect<Equal<PartialByKeys<User>, Partial<User>>>
];

// ============= Your Code Here =============
type PartialByKeys1<T, K = keyof T> = {
  [P in keyof ({
    // Only need keys here, so no need to add `: T[P]`
    [P in keyof T as P extends K ? P : never]?;
  } & {
    [P in keyof T as P extends K ? never : P];
    // T[P] works because the change to partial will auto-have `undefined`
  })]: T[P];
};

// https://ghaiklor.github.io/type-challenges-solutions/en/medium-partialbykeys.html
// take advantage of `Distributive Conditional Types`
type MyMerge<T> = { [P in keyof T]: T[P] };

type PartialByKeys<T, K = keyof T> = MyMerge<
  {
    [P in keyof T as P extends K ? P : never]?: T[P];
  } & {
    [P in keyof T as P extends K ? never : P]: T[P];
  }
>;
