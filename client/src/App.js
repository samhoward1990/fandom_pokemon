import React from 'react'
import { useState, useEffect } from 'react'

function App() {

  const [data, getData] = useState([{}]);

  useEffect(() => {
    fetch('/testdata').then(
      res => res.json()
      ).then(
        data => {
          getData(data)
      }, []);
  })
  return (
    <div>
      <h1>Fandom Pokemon</h1>
      <h2>{data.name}</h2>
      <ul>
        <li>Type: {data.type}</li>
        <li>HP: {data.hp}</li>
        <li>Defense: {data.defense}</li>
        <li>Offense: {data.attack}</li>
      </ul>

    </div>
  )
}

export default App