// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

interface User {
  name?: string;
  age?: number;
  address?: string;
}

interface UserRequiredName {
  name: string;
  age?: number;
  address?: string;
}

interface UserRequiredNameAndAge {
  name: string;
  age: number;
  address?: string;
}

type cases = [
  Expect<Equal<RequiredByKeys<User, "name">, UserRequiredName>>,
  Expect<Equal<RequiredByKeys<User, "name" | "unknown">, UserRequiredName>>,
  Expect<Equal<RequiredByKeys<User, "name" | "age">, UserRequiredNameAndAge>>,
  Expect<Equal<RequiredByKeys<User>, Required<User>>>
];

// ============= Your Code Here =============
type RequiredByKeys1<T, K = keyof T> = {
  [P in keyof ({
    [P in keyof T as P extends K ? P : never]-?;
  } & {
    [P in keyof T as P extends K ? never : P];
    // `T[P] extends infer R | undefined ? R : T[P]` removes the partial's undefined type value
    // Has `Type 'P' cannot be used to index type 'T'.` here, don't know why
  })]: T[P] extends infer R | undefined ? R : T[P];
};

// https://ghaiklor.github.io/type-challenges-solutions/en/medium-requiredbykeys.html
// take advantage of `Distributive Conditional Types`
type MyMerge<T> = { [P in keyof T]: T[P] };

type RequiredByKeys<T, K = keyof T> = MyMerge<
  {
    [P in keyof T as P extends K ? P : never]-?: T[P];
  } & {
    [P in keyof T as P extends K ? never : P]: T[P];
  }
>;
