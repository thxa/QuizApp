import React, { useState } from 'react';

function Quiz({
    questions,
    currentQuestionIndex,
    score,
    setScore,
    correctAnswers,
    setCorrectAnswers,
    selectedOptions,
    setSelectedOptions,
    handlePrevQuestion,
    handleNextQuestion,
}) {
    const question = questions[currentQuestionIndex];
    const [clickedButtonIndex, setClickedButtonIndex] = useState(null);
    const [buttonClass, setButtonClass] = useState(null);

    const selectAnswer = (index, isCorrect) => {
        setSelectedOptions(selectedOptions + 1);
        if (isCorrect) {
            setButtonClass('correct');
            setCorrectAnswers(correctAnswers + 1);
        } else {
            setButtonClass('incorrect');
        }
        if (correctAnswers === question.answers.length-1) {
            setScore(score + 1);

        }

        setClickedButtonIndex(index);
        // console.log(isCorrect)

    };

    return (
        <div className="quiz">
        <h2>{currentQuestionIndex + 1}. {question.question}</h2>
        <div id="options-btns">
        {question.options.map((option, index) => (
            <button
            key={index}
            className={`btn ${clickedButtonIndex === index ?  buttonClass : ""}`}
            onClick={() => selectAnswer(index, question.answers.includes(index + 1))} 
            disabled={selectedOptions >= question.answers.length}
            >
            {option}
            </button>
        ))}
        </div>



        { 
            currentQuestionIndex > 0 ? 
            <button 
            id="next-btn" 
            onClick={handlePrevQuestion}
            > Prev </button> 
            : ""
        }

        <button id="next-btn" onClick={handleNextQuestion}>
        {currentQuestionIndex < questions.length - 1 ? 'Next' : 'Play Again'}
        </button>

        </div>
    );
}

export default Quiz;

