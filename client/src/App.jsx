import { useEffect, useState } from 'react'

import './App.css'

function App() {
  const [web, setWeb] = useState([])

  useEffect(() => {
    fetch('/api')
    .then(resp => resp.json())
    .then(data => 
      setWeb(data))
  }, [])

  return (
    <>
      <div>
        <h1>Here are my apis</h1>
        <h1>{web}</h1>
        </div>
    </>
  )
}

export default App
