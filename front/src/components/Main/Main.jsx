import React, { useState } from 'react';
import axios from 'axios';
import './Main.css'

function Main() {
  const [text, setText] = useState('');
  const [count, setCount] = useState('');
  const [data, setData] = useState();
  const [response, setResponse] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.get(`http://localhost:5000/submit?text=${text}&count=${count}`);
      const data = response.data;
      setData(data)
      setResponse(true)
      console.log(data)
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <>
      <h1 className="headerOverlap">Extractive Text Summarizer</h1>
      <div className="split left">
        <div className="centered">
          <h2 className="headerIn">Input</h2>
          <p className="instructionsTop">Enter full text:</p>
          <form onSubmit={handleSubmit}>
            <textarea
              className="textbox"
              value={text}
              onChange={(e) => setText(e.target.value)}
            />
            <div className="input-container">
              <p className="instructionsBtm">Enter outputted sentence count:</p>
              <input
                className="valuebox"
                value={count}
                onChange={(e) => {
                  const input = e.target.value;
                  if (/^\d{0,2}$/.test(input)) {
                    setCount(input);
                  }
                }}
                maxLength={2}
              />
            </div>
            <button className="button" type="submit">Submit</button>
          </form>
        </div>
      </div>
    
      <div className="split right">
        <div className="centered">
        {response && (
            <>
              <h2 className="header">Output</h2>
              <div className="rougeScoresContainer">
                <div className="rougeScore">
                  <h3>ROUGE-1:</h3>
                  <ul>
                    <li>Precision: <span className="rougeScoreValue">{(data.rougeScores[0]['rouge-1'].p * 100).toFixed(2)}%</span></li>
                    <li>Recall: <span className="rougeScoreValue">{(data.rougeScores[0]['rouge-1'].r * 100).toFixed(2)}%</span></li>
                    <li>F1 Score: <span className="rougeScoreValue">{(data.rougeScores[0]['rouge-1'].f * 100).toFixed(2)}%</span></li>
                  </ul>
                </div>
                <div className="rougeScore">
                  <h3>ROUGE-2:</h3>
                  <ul>
                    <li>Precision: <span className="rougeScoreValue">{(data.rougeScores[0]['rouge-2'].p * 100).toFixed(2)}%</span></li>
                    <li>Recall: <span className="rougeScoreValue">{(data.rougeScores[0]['rouge-2'].r * 100).toFixed(2)}%</span></li>
                    <li>F1 Score: <span className="rougeScoreValue">{(data.rougeScores[0]['rouge-2'].f * 100).toFixed(2)}%</span></li>
                  </ul>
                </div>
                <div className="rougeScore">
                  <h3>ROUGE-L:</h3>
                  <ul>
                    <li>Precision: <span className="rougeScoreValue">{(data.rougeScores[0]['rouge-l'].p * 100).toFixed(2)}%</span></li>
                    <li>Recall: <span className="rougeScoreValue">{(data.rougeScores[0]['rouge-l'].r * 100).toFixed(2)}%</span></li>
                    <li>F1 Score: <span className="rougeScoreValue">{(data.rougeScores[0]['rouge-l'].f * 100).toFixed(2)}%</span></li>
                  </ul>
                </div>
              </div>
              <ul className='outputSentenceParent'>
                {data.sentenceWeights.map((item, index) => (
                  <li className="outputSentence" key={index}>{item.sentence}</li>
                ))}
              </ul>
            </>
          )}
        </div>
      </div>
    </>
  );
}

export default Main;