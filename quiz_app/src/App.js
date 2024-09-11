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


import React, { useState, useEffect } from 'react';
import './App.css';
import StartMenu from './StartMenu';
import Quiz from './Quiz';
import LoadingScreen from './LoadingScreen';

function App() {
  const [questions, setQuestions] = useState([]);
  const [quizStarted, setQuizStarted] = useState(false);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [loading, setLoading] = useState(true);
  const [score, setScore] = useState(0);
  const [correctAnswers, setCorrectAnswers] = useState(0);
  const [selectedOptions, setSelectedOptions] = useState(0);

  useEffect(() => {
    fetch("Edited_quiz_1_cleaned_1.json")
      .then(res => res.json())
      .then(data => {
        setQuestions(data);
        setLoading(false);
      })
      .catch(err => {
        alert("could not reach the questions file")
        console.error(err);
        setLoading(false);
      });
  }, []);

  const startQuiz = (numberOfQuestions) => {
    setCurrentQuestionIndex(0);
    setScore(0);
    setCorrectAnswers(0);
    setSelectedOptions(0);
    setQuizStarted(true);
    setQuestions(prevQuestions => prevQuestions.slice(0, numberOfQuestions));
  };

  const handleNextQuestion = () => {
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(prevIndex => prevIndex + 1);
      setSelectedOptions(0);
      setCorrectAnswers(0);
    } else {
      setQuizStarted(false);
    }
  };


const handlePrevQuestion = () => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(prevIndex => prevIndex - 1);
      setSelectedOptions(0);
      setCorrectAnswers(0);
    }
  };


  return (
    <div className="app">
      

      {loading ? (
        <LoadingScreen />
      ) : (
        <>
          <h1>Quiz App</h1>
          <div id="question_size">{questions.length}</div>
          {quizStarted ? (
            <Quiz
              questions={questions}
              currentQuestionIndex={currentQuestionIndex}
              score={score}
              setScore={setScore}
              correctAnswers={correctAnswers}
              setCorrectAnswers={setCorrectAnswers}
              selectedOptions={selectedOptions}
              setSelectedOptions={setSelectedOptions}
              handlePrevQuestion={handlePrevQuestion}
              handleNextQuestion={handleNextQuestion}
            />
          ) : (
            <StartMenu startQuiz={startQuiz} />
          )}
        </>
      )}

    </div>
  );
}

export default App;

