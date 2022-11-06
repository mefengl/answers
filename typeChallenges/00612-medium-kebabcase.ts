// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

type cases = [
  Expect<Equal<KebabCase<"FooBarBaz">, "foo-bar-baz">>,
  Expect<Equal<KebabCase<"fooBarBaz">, "foo-bar-baz">>,
  Expect<Equal<KebabCase<"foo-bar">, "foo-bar">>,
  Expect<Equal<KebabCase<"foo_bar">, "foo_bar">>,
  Expect<Equal<KebabCase<"Foo-Bar">, "foo--bar">>,
  Expect<Equal<KebabCase<"ABC">, "a-b-c">>,
  Expect<Equal<KebabCase<"-">, "-">>,
  Expect<Equal<KebabCase<"">, "">>,
  Expect<Equal<KebabCase<"😎">, "😎">>
];

// ============= Your Code Here =============
// add - for every capital char, even the first one
type KebabCase1<S> = S extends `${infer H}${infer T}`
  ? H extends keyof Capitalize<H>
    ? `-${Capitalize<H>}${KebabCase1<T>}`
    : `${H}${KebabCase1<T>}`
  : S;

// https://ghaiklor.github.io/type-challenges-solutions/en/medium-kebabcase.html
// from T, then H is skipped by default
type KebabCase<S> = S extends `${infer H}${infer T}`
  ? // get first Char in Tail
    T extends Uncapitalize<T>
    ? `${Uncapitalize<H>}${KebabCase<T>}`
    : `${Uncapitalize<H>}-${KebabCase<T>}`
  : S;
