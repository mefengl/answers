import { gql, useQuery } from "@apollo/client"

const ALL_PERSONS = gql`
  query {
    personCount
  }
`

export default function Home() {
  const result = useQuery(ALL_PERSONS)
  console.log(result)

  if (result.loading) {
    return <div>loading...</div>
  }

  return (
    <div>
    hello
    </div>
  )
}
