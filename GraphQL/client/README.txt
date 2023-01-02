nextjs + tailwindcss
https://tailwindcss.com/docs/guides/nextjs

npx create-next-app@latest my-project --typescript --eslint
cd my-project
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

vim tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

vim globals.css
@tailwind base;
@tailwind components;
@tailwind utilities;

apollo client
npm i @apollo/client graphql

vim pages/_app.tsx
import { ApolloClient, ApolloProvider, HttpLink, InMemoryCache } from "@apollo/client"
const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: new HttpLink({
    uri: "http://localhost:4000",
  }),
})

export default function App({ Component, pageProps }: AppProps) {
  return <ApolloProvider client={client}>
    <Component {...pageProps} />
  </ApolloProvider>
}

vim pages/index.tsx
import { gql, useQuery } from "@apollo/client"
const GET_POSTS = gql`
  query GetPosts {
    posts {
      id
      title
      body
    }
  }
`

export default function Home() {
  const { data, loading, error } = useQuery(GET_POSTS)
  if (loading) return <div>loading...</div>
  if (error) return <div>error</div>
  return <div>
    {data.posts.map((post: any) => <div key={post.id}>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </div>)}
  </div>
}
