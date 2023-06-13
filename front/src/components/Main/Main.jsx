import React, { useState } from 'react';
import axios from 'axios';
import './Main.css'

function Main() {
  const [value, setValue] = useState('');
  const [data, setData] = useState();
  const [response, setResponse] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.get(`http://localhost:5000/submit?value=${value}`);
      const data = response.data;
      setData(data)
      setResponse(true);
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <>
      <h1 className="headerOverlap">Extractive Text Summarizer</h1>
      <div className="split left">
        <div className="centered">
          <h2 className="header">Input</h2>
          <form onSubmit={handleSubmit}>
            <textarea
              className="textbox"
              value={value}
              onChange={(e) => setValue(e.target.value)}
            />
            <button className="button" type="submit">Submit</button>
          </form>
        </div>
      </div>
    
      <div className="split right">
        <div className="centered">
          <h2 className="header">Output</h2>
          {/* { response && (
            <p className="receivedText"><b>RECEIVED RESPONSE:</b><br/>{data}</p>
          )} */}
          <p className="receivedText">Heeeyyyyy</p>
        </div>
      </div>
    </>
  );
}

export default Main;