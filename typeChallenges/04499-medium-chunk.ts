// ============= Test Cases =============
import type { Equal, Expect } from './test-utils'

type cases = [
  Expect<Equal<Chunk<[], 1>, []>>,
  Expect<Equal<Chunk<[1, 2, 3], 1>, [[1], [2], [3]]>>,
  Expect<Equal<Chunk<[1, 2, 3], 2>, [[1, 2], [3]]>>,
  Expect<Equal<Chunk<[1, 2, 3, 4], 2>, [[1, 2], [3, 4]]>>,
  Expect<Equal<Chunk<[1, 2, 3, 4], 5>, [[1, 2, 3, 4]]>>,
  Expect<Equal<Chunk<[1, true, 2, false], 2>, [[1, true], [2, false]]>>,
]


// ============= Your Code Here =============
type Chunk<T extends unknown[], N, Swap extends unknown[] = []> =
  Swap['length'] extends N ?
  [Swap, ...Chunk<T, N>]
  : T extends [infer F, ...infer R]
  ? Chunk<R, N, [...Swap, F]>
  // if it's empty, `...Swap` will turn it into never,
  // if not, `...[Swap]` protect Swap itself
  : Swap extends [] ? Swap : [Swap]

type zz = Chunk<[1, 2, 3], 2>
