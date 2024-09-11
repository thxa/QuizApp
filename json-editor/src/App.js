// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

import React, { useState } from 'react';
import JSONEditor from './JSONEditor';
import './style.css';

function App() {
  const [jsonData, setJsonData] = useState([]);
  const [fileName, setFileName] = useState("edited_json.json");

  const handleFileUpload = (event) => {
    setFileName(event.target.files[0].name)
    console.log(event.target.files[0])
      const fileReader = new FileReader();
    fileReader.onload = () => {
      setJsonData(JSON.parse(fileReader.result));
    };
    fileReader.readAsText(event.target.files[0]);
    
  };

  const handleJsonChange = (index, updatedItem) => {
    const newData = [...jsonData];
    newData[index] = updatedItem;
    setJsonData(newData);
  };

  const saveToFile = () => {
    const fileData = JSON.stringify(jsonData, null, 2);
    const blob = new Blob([fileData], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `Edited_${fileName}`;
    link.click();
  };

  return (
    <div className="App">
      <h1>JSON Editor</h1>
      <input type="file" accept=".json" onChange={handleFileUpload} />
      {jsonData.map((item, index) => (
        <JSONEditor
          key={index}
          data={item}
          onChange={(updatedItem) => handleJsonChange(index, updatedItem)}
        />
      ))}
      <button onClick={saveToFile}>Save JSON</button>
    </div>
  );
}

export default App;
