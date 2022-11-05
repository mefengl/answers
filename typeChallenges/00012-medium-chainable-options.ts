// ============= Test Cases =============
import type { Alike, Expect, ExpectExtends } from "./test-utils";

declare const a: Chainable;

const result1 = a
  .option("foo", 123)
  .option("bar", { value: "Hello World" })
  .option("name", "type-challenges")
  .get();

const result2 = a
  .option("name", "another name")
  // @ts-expect-error
  .option("name", "last name")
  .get();

const result3 = a.option("name", "another name").option("name", 123).get();

type cases = [
  Expect<Alike<typeof result1, Expected1>>,
  Expect<Alike<typeof result2, Expected2>>,
  Expect<Alike<typeof result3, Expected3>>
];

type Expected1 = {
  foo: number;
  bar: {
    value: string;
  };
  name: string;
};

type Expected2 = {
  name: string;
};

type Expected3 = {
  name: number;
};

// ============= Your Code Here =============
type Chainable1<O = {}> = {
  option<K extends string, V>(
    key: K extends keyof O ? (V extends O[K] ? never : K) : K,
    value: V
  ): Chainable1<
    // Can't make it, later key need to overwrite the previous one
    O & { [P in K]: V }
  >;
  get(): O;
};

type Chainable2<O = {}> = {
  option<K extends string, V>(
    key: K,
    value: V
  ): Chainable2<
    // one more thing, the latter key overwrites the previous one should only when the value type is different
    { [P in keyof O as P extends K ? never : P]: O[P] } & { [P in K]: V }
  >;
  get(): O;
};

// full version with functions
type MyRecord<K extends string, V> = {
  [P in K]: V;
};

type MyOmit<K, V> = {
  [P in keyof K as P extends V ? never : P]: K[P];
};

type MyMatch<K, O, V> = K extends keyof O
  ? V extends O[K]
    ? false
    : true
  : true;

type Chainable3<O = {}> = {
  option<K extends string, V>(
    key: MyMatch<K, O, V> extends true ? K : never,
    value: V
  ): Chainable3<MyRecord<K, V> & MyOmit<O, K>>;
  get(): O;
};

// full version
type Chainable<O = {}> = {
  option<K extends string, V>(
    key: K extends keyof O ? (V extends O[K] ? never : K) : K,
    value: V
  ): Chainable<
    { [P in K]: V } & { [P in keyof O as P extends K ? never : P]: O[P] }
  >;
  get(): O;
};
