var questions;
var questions_x;

// loadingScreen
const loading_screen = document.getElementById("loading-screen");


// start menu elements
const start_quiz_btn = document.getElementById("start_quiz");
const start_element = document.getElementById("start");
const question_size = document.getElementById("question_size");

// quiz elements
const question_element = document.getElementById("question");
const options_btns = document.getElementById("options-btns");
const next_btn = document.getElementById("next-btn");

const resources_element = document.getElementById("resources");

let curr_q_i = 0;
let score = 0;
let correct_answers = 0;
let selected_options = 0;

function get_data() {

    loading_screen.style.display = "block";

    fetch("output/Edited_quiz_1_cleaned_1.json")
        .then((res) => res.json())
        .then((json) => {
            questions = json;
            question_size.innerHTML = questions.length+"";

            loading_screen.style.display = "none";
        })
        .catch((e) => { 

            loading_screen.style.display = "none";
            console.error(e); 

        });
}

function reset_question() {
    next_btn.style.display = "none";
    while(options_btns.firstChild) {
        options_btns.removeChild(options_btns.firstChild);
    }
    while(resources_element.firstChild) {
        resources_element.removeChild(resources_element.firstChild);
    }

}

function show_question() {
    let curr_q = questions[curr_q_i];
    let question_i = curr_q_i + 1;
    let a_i = 0;

    selected_options = 0;
    correct_answers = 0;

    question_element.innerHTML = question_i + ". " + curr_q.question;

    curr_q.options.forEach(option => {
        const btn = document.createElement("button");
        btn.innerHTML = option;
        btn.classList.add("btn");
        options_btns.appendChild(btn);

        // if(option.correct) {
        //     btn.dataset.correct = option.correct;
        // }
        
        if(curr_q["answers"].indexOf(a_i+1) !== -1) {
            btn.dataset.correct = true;
        } else {
            btn.dataset.correct = false;
        }

        btn.addEventListener("click", select_answer);


        a_i++;
    });



}

function start_quiz() {
    curr_q_i = 0;
    score = 0;
    next_btn.innerHTML = "Next";
    start_element.style.display = "none";
    show_question();
}

function select_answer(e) {
    const selected_btn = e.target;
    const is_correct = selected_btn.dataset.correct === "true";
    let curr_q = questions[curr_q_i];
    selected_options++;
    if(is_correct) {
        selected_btn.classList.add("correct");
        correct_answers++;
    } else {
        selected_btn.classList.add("incorrect");
    }
    
    if(correct_answers == curr_q["answers"].length) {
        score++;
    }

    if(selected_options == curr_q["answers"].length) {
        Array.from(options_btns.children).forEach(btn => {
            if(btn.dataset.correct === "true"){
                btn.classList.add("correct");
            }
            btn.disabled = true;
        });

        
        // display the resources urls
        curr_q["resources"].forEach(resource => {

            let p = document.createElement("p");
            p.innerHTML=`<a href="${resource}" class="dropdown-item" target="_blank">${resource}</a>`
            resources_element.appendChild(p);

        });



        next_btn.style.display = "block";
    }


}

function show_score() {
    reset_question();
    question_element.innerHTML = `Your socre is ${score}/${questions.length}`;
    next_btn.innerHTML = "Play Again";
    next_btn.style.display = "block";

}

function handle_next_btn() {
    curr_q_i++;
    if(curr_q_i < questions.length) {
        reset_question();
        show_question();
    } else {
        show_score();
    }
    
}

next_btn.addEventListener("click", ()=>{
    if(curr_q_i < questions.length) {
        handle_next_btn();
    } else {
         location.reload(); 
        // start_quiz();
    }
})


start_quiz_btn.addEventListener("click", ()=>{
    start_quiz();
})






// main
get_data()

// start_quiz()
