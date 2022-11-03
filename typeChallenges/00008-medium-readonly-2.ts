// ============= Test Cases =============
import type { Alike, Expect } from './test-utils'

type cases = [
  Expect<Alike<MyReadonly2<Todo1>, Readonly<Todo1>>>,
  Expect<Alike<MyReadonly2<Todo1, 'title' | 'description'>, Expected>>,
  Expect<Alike<MyReadonly2<Todo2, 'title' | 'description'>, Expected>>,
]

// @ts-expect-error
type error = MyReadonly2<Todo1, 'title' | 'invalid'>

interface Todo1 {
  title: string
  description?: string
  completed: boolean
}

interface Todo2 {
  readonly title: string
  description?: string
  completed: boolean
}

interface Expected {
  readonly title: string
  readonly description?: string
  completed: boolean
}


// ============= Your Code Here =============
// like in JS, K = keyof T means when no K is given, K = keyof T
// not like in JS, & means the 'and' in 'you and me'
// type MyReadonly2<T, K extends keyof T = keyof T> = {
//   readonly [P in K]: T[P];
// } & { [P in keyof T as P extends K ? never : P]: T[P] };

// mutil function
// type MyReadonly2<T, K extends keyof T = keyof T> = Omit<T, K> & Readonly<T>;
type MyReadonly<T> = {
  readonly [P in keyof T]: T[P];
};
type MyOmit<T, K> = {
  [P in keyof T as P extends K ? never : P]: T[P];
};
// here can't use MyReadonly<K>, because K is just a key list
type MyReadonly2<T, K extends keyof T = keyof T> = MyReadonly<T> & MyOmit<T,K>
