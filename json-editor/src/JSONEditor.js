import React, { useState } from 'react';

function JSONEditor({ data, onChange }) {
  const [item, setItem] = useState(data);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    const updatedItem = {
      ...item,
      [name]: Array.isArray(item[name]) ? value.split(',') : value,
    };
    setItem(updatedItem);
    onChange(updatedItem);
  };

  return (
    <div className="json-editor">
      <label>ID:</label>
      <input
        type="text"
        name="_id"
        value={item._id}
        onChange={handleInputChange}
      />
      <label>Question:</label>
      

      <textarea
        name="question"
        value={item.question}
        onChange={handleInputChange}
      />

      <label>Options:</label>
      <textarea
        name="options"
        value={item.options.join('\n')}
        onChange={handleInputChange}
      />

      <label>Explain:</label>
      <textarea
        name="explain"
        value={item.explain}
        onChange={handleInputChange}
      />



      <label>Answers:</label>
      <input
        type="text"
        name="answers"
        value={item.answers.join(',')}
        onChange={handleInputChange}
      />
      <label>Resources:</label>
      <textarea
        name="resources"
        value={item.resources.join('\n')}
        onChange={handleInputChange}
      />
    </div>
  );
}

export default JSONEditor;

