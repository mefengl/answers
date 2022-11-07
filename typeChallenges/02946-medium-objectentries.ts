// ============= Test Cases =============
import type { Equal, Expect, ExpectExtends } from "./test-utils";

interface Model {
  name: string;
  age: number;
  locations: string[] | null;
}

type ModelEntries =
  | ["name", string]
  | ["age", number]
  | ["locations", string[] | null];

type cases = [
  Expect<Equal<ObjectEntries<Model>, ModelEntries>>,
  Expect<Equal<ObjectEntries<Partial<Model>>, ModelEntries>>,
  Expect<Equal<ObjectEntries<{ key?: undefined }>, ["key", undefined]>>,
  Expect<Equal<ObjectEntries<{ key: undefined }>, ["key", undefined]>>
];

// ============= Your Code Here =============
// https://ghaiklor.github.io/type-challenges-solutions/en/medium-objectentries.html
type ObjectEntries<T> = {
  // `-?` is for the undefined[any] = undefined case
  // like in `Expect<Equal<ObjectEntries<{ key?: undefined }>, ["key", undefined]>>`, will see `["key", undefined] | undefined`
  // `T[P] extends infer R | undefined ? R : T[P]` removes the partial's undefined type value
  [P in keyof T]-?: [P, T[P] extends infer R | undefined ? R : T[P]];
}[keyof T];
