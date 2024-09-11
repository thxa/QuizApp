import React, { useState } from 'react';

function StartMenu({ startQuiz }) {
  const [numberOfQuestions, setNumberOfQuestions] = useState(10);

  return (
    <div id="start">
      <label htmlFor="number_of_question">Number of Questions</label>
      <input
        id="number_of_question"
        type="number"
        value={numberOfQuestions}
        onChange={(e) => setNumberOfQuestions(e.target.value)}
        placeholder="10"
      />
      <br />
      <button
        id="start_quiz"
        className="start-btn"
        onClick={() => startQuiz(numberOfQuestions)}
      >
        Start
      </button>
    </div>
  );
}

export default StartMenu;

