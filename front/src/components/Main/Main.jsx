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
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          className='textbox'
          value={value}
          onChange={(e) => setValue(e.target.value)}
        />
        <button type="submit">Submit</button>
        { response && (
          <p><b>RECEIVED RESPONSE:</b><br></br>{data}</p>
        )}
      </form>
    </div>
  );
}

export default Main;