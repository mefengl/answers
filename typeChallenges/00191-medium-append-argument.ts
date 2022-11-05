// ============= Test Cases =============
import type { Equal, Expect } from "./test-utils";

type Case1 = AppendArgument<(a: number, b: string) => number, boolean>;
type Result1 = (a: number, b: string, x: boolean) => number;

type Case2 = AppendArgument<() => void, undefined>;
type Result2 = (x: undefined) => void;

type cases = [Expect<Equal<Case1, Result1>>, Expect<Equal<Case2, Result2>>];

// ============= Your Code Here =============
// function is 'function(arg: P): infer R'
// arrow function is '(arg: P) => infer R'
type AppendArgument1<Fn, A> = Fn extends (args: infer P) => infer R
  ? (args: P) => R
  : never;

type AppendArgument2<Fn, A> = Fn extends (...args: [...infer P]) => infer R
  ? (...args: [...P]) => R
  : never;

type AppendArgument<Fn, A> = Fn extends (...args: [...infer P]) => infer R
  ? (...args: [...P, A]) => R
  : never;
