import { useState } from 'react'
import { TextInput, Button, Paper, Text } from '@mantine/core';
import axios from 'axios';
import { Routes, Route } from 'react-router-dom';

function App() {

  const getResponse = async () => {
    try{
      const output = await axios.post( 'http://localhost:8000/api/validate/',
        {
          text : input
        }
       )
      //  console.log( output.data );
       setResponse( output.data )
    }
    catch ( err ){
      console.log( "error in api call:\n", err );
    }
  }


  const [ input, setInput ] = useState( "" )
  const [ response, setResponse ] = useState( null )
  
  return (
    <>
    <div style={{ marginTop: '40px' }}>
      <TextInput
        size="xl"
        radius="xl"
        label="AI Text"
        withAsterisk
        placeholder="Enter text"
        onChange = { ( e ) => {
          setInput( e.target.value)
          console.log( e.target.value )
          }
        }
      />
    </div>
    <div style={{ marginTop: '40px' }}>
      <Button variant="filled" size="xl" radius="xl" disabled = { input.length == 0 } onClick = { getResponse } >Submit</Button>
    </div>
    <div style={{ marginTop: '40px' }}>
      <Paper shadow="xs" radius="xl" withBorder p="xl">
      <Text>Evaluated Response</Text>
      <Text>
        <pre style={{ margin: 0, whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>
          {JSON.stringify(response, null, 2)}
        </pre>
      </Text>
    </Paper>
    </div>
    </>
  )
}

export default App
