import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';
import { v1 as uuid } from 'uuid';
import mongoose from 'mongoose';
import Person from './models/person.js';
import env from './env.json' assert { type: 'json' };
const MONGODB_URI = `mongodb+srv://dbUser:${env.pw}@cluster0.84pbcs2.mongodb.net/?retryWrites=true&w=majority`
console.log('connecting to', MONGODB_URI)

mongoose.connect(MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    console.log('connected to MongoDB')
  })
  .catch((error) => {
    console.log('error connecting to MongoDB:', error.message)
  })

const typeDefs = `#graphql
enum YesNo {
  YES
  NO
}

type Address {
  street: String!
  city: String! 
}

  type Person {
    name: String!
    phone: String
    address: Address!
    id: ID!
  }

  type Query {
    personCount: Int!
    allPersons(phone: YesNo): [Person!]!
    findPerson(name: String!): Person
  }

  type Mutation {
    addPerson(
      name: String!
      phone: String
      street: String!
      city: String!
    ): Person
    editNumber(
      name: String!
      phone: String!
    ): Person
  }
`

const resolvers = {
  Query: {
    personCount: async () => Person.collection.countDocuments(),
    allPersons: async (root, args) => {
      return Person.find({})
    },
    findPerson: async (root, args) =>
      Person.findOne({ name: args.name })
  },
  Mutation: {
    addPerson: async (root, args) => {
      const person = new Person({ ...args })
      return person.save()
    },
    editNumber: async (root, args) => {
      const person = await Person.findOne({ name: args.name })
      person.phone = args.phone
      return person.save()
    }
  },
  Person: {
    address: (root) => {
      return {
        street: root.street,
        city: root.city
      }
    }
  }
}

const server = new ApolloServer({
  typeDefs,
  resolvers
});

const { url } = await startStandaloneServer(server);
console.log(`🚀 Server ready at ${url}`);
