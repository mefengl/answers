import { gql, useQuery } from "@apollo/client"

const ALL_PERSONS = gql`
  query {
    allPersons {
      name
    }
  }
`

export default function Home() {
  const result = useQuery(ALL_PERSONS)

  if (result.loading) {
    return <div>loading...</div>
  }

  return (
    <div>
      {result.data.allPersons.map((p: any) => p.name).join(", ")}
    </div>
  )
}
