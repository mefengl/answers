// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

type Foo = {
  name: string;
  age: string;
};
type Bar = {
  name: string;
  age: string;
  gender: number;
};
type Coo = {
  name: string;
  gender: number;
};

type cases = [
  Expect<Equal<Diff<Foo, Bar>, { gender: number }>>,
  Expect<Equal<Diff<Bar, Foo>, { gender: number }>>,
  Expect<Equal<Diff<Foo, Coo>, { age: string; gender: number }>>,
  Expect<Equal<Diff<Coo, Foo>, { age: string; gender: number }>>
];

// ============= Your Code Here =============
// O minus O1
type Diff1<O, O1> = {
  [K in keyof O as K extends keyof O1 ? never : K]: O[K];
};

// { O minus O1 } | { O1 minus O }
// | means 'both have'
type Diff2<O, O1> = {
  [K in keyof O | keyof O1 as K extends keyof O1
    ? K extends keyof O
      ? never
      : K
    : K]: K extends keyof O ? O[K] : K extends keyof O1 ? O1[K] : never;
};

// O&O1 - O|O1
// & means 'either has', | means 'both have'
type Diff<O, O1> = {
  [K in keyof (O & O1) as K extends keyof (O | O1) ? never : K]: (O & O1)[K];
};
