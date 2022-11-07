// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

type cases = [
  // @ts-expect-error
  Expect<Equal<DropChar<"butter fly!", "">, "butterfly!">>,
  Expect<Equal<DropChar<"butter fly!", " ">, "butterfly!">>,
  Expect<Equal<DropChar<"butter fly!", "!">, "butter fly">>,
  Expect<Equal<DropChar<"    butter fly!        ", " ">, "butterfly!">>,
  Expect<Equal<DropChar<" b u t t e r f l y ! ", " ">, "butterfly!">>,
  Expect<Equal<DropChar<" b u t t e r f l y ! ", "b">, "  u t t e r f l y ! ">>,
  Expect<Equal<DropChar<" b u t t e r f l y ! ", "t">, " b u   e r f l y ! ">>
];

// ============= Your Code Here =============
// check them one by one
type DropChar1<S, C> = S extends `${infer F}${infer R}`
  ? F extends C
    ? DropChar1<R, C>
    : `${F}${DropChar1<R, C>}`
  : S;

// delete them one by one, from https://ghaiklor.github.io/type-challenges-solutions/en/medium-drop-char.html
type DropChar<S, C extends string> = S extends `${infer L}${C}${infer R}`
  ? `${L}${DropChar<R, C>}`
  : S;
