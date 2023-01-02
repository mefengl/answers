https://fullstackopen.com/en/part8

https://github.com/apollographql/apollo-server#getting-started-standalone-server
npm i @apollo/server graphql

```js
import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';

const server = new ApolloServer({ 
  typeDefs: `#graphql
    type Query {
      hello: String
    }
  `, 
  resolvers: {
    Query: { hello: () => 'world' },
  } 
});

const { url } = await startStandaloneServer(server);
console.log(`🚀 Server ready at ${url}`);
```

different types of resolvers
Query
Person, can rewrite the default resolver of a value,
```js
  // if there is a Person type, it will be resolved like this in the background
  Person: {
    name: (root) => root.name,
    street: (root) => root.street,
    city: (root) => root.city,
  },
  // that is why we can change the default resolver like this
  Person: {
    // name: (root) => root.name,
    address: (root) => {
      return {
        street: root.street,
        city: root.city,
      };
    },
  },
```
Mutation,
```js
  Mutation: {
    addPerson: (root, args) => {
      const person = { ...args, id: uuid() }
      persons = persons.concat(person)
      return person
    }
  },
```
