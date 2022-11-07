// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

type Foo = {
  [key: string]: any;
  foo(): void;
};

type Bar = {
  [key: number]: any;
  bar(): void;
  0: string;
};

const foobar = Symbol("foobar");
type FooBar = {
  [key: symbol]: any;
  [foobar](): void;
};

type Baz = {
  bar(): void;
  baz: string;
};

type cases = [
  Expect<Equal<RemoveIndexSignature<Foo>, { foo(): void }>>,
  Expect<Equal<RemoveIndexSignature<Bar>, { bar(): void; 0: string }>>,
  Expect<Equal<RemoveIndexSignature<FooBar>, { [foobar](): void }>>,
  Expect<Equal<RemoveIndexSignature<Baz>, { bar(): void; baz: string }>>
];

// ============= Your Code Here =============
// https://github.com/ghaiklor/type-challenges-solutions/issues/185#issuecomment-1076124609
// only string literally can fit `${infer _}`, doesn't work on 0,1,2... or symbol
type RemoveIndexSignature1<T> = {
  [K in keyof T as K extends `${infer _}` ? K : never]: T[K];
};

// “foo” is too narrow to be a string, from https://ghaiklor.github.io/type-challenges-solutions/en/medium-remove-index-signature.html
type RemoveIndexSignature<T> = {
  [K in keyof T as string extends K
    ? never
    : number extends K
    ? never
    : symbol extends K
    ? never
    : K]: T[K];
};
