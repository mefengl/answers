// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

type cases = [
  Expect<Equal<ReplaceAll<"foobar", "bar", "foo">, "foofoo">>,
  Expect<Equal<ReplaceAll<"foobar", "bag", "foo">, "foobar">>,
  Expect<Equal<ReplaceAll<"foobarbar", "bar", "foo">, "foofoofoo">>,
  Expect<Equal<ReplaceAll<"t y p e s", " ", "">, "types">>,
  Expect<Equal<ReplaceAll<"foobarbar", "", "foo">, "foobarbar">>,
  Expect<Equal<ReplaceAll<"barfoo", "bar", "foo">, "foofoo">>,
  Expect<Equal<ReplaceAll<"foobarfoobar", "ob", "b">, "fobarfobar">>,
  Expect<Equal<ReplaceAll<"foboorfoboar", "bo", "b">, "foborfobar">>,
  Expect<Equal<ReplaceAll<"", "", "">, "">>
];

// ============= Your Code Here =============
type ReplaceAll1<
  S extends string,
  From extends string,
  To extends string
> = S extends `${infer L}${From}${infer R}` ? `${L}${To}${R}` : S;

type ReplaceAll2<
  S extends string,
  From extends string,
  To extends string
> = S extends `${infer L}${From}${infer R}`
  ? ReplaceAll2<`${L}${To}${R}`, From, To>
  : S;

type ReplaceAll3<
  S extends string,
  From extends string,
  To extends string
> = From extends ""
  ? S
  : S extends `${infer L}${From}${infer R}`
  ? ReplaceAll3<`${L}${To}${R}`, From, To>
  : S;

// https://ghaiklor.github.io/type-challenges-solutions/en/medium-replaceall.html
type ReplaceAll<
  S extends string,
  From extends string,
  To extends string,
  Begin extends string = ""
> = From extends ""
  ? S
  : S extends `${Begin}${infer L}${From}${infer R}`
  ? ReplaceAll<`${Begin}${L}${To}${R}`, From, To, `${Begin}${L}${To}`>
  : S;
