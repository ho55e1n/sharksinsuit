var questions = [
  new Question(
    "Which language is regarded as the de facto national language of Australia?",
    ["German", "English", "Hindi", "Mandarin"],
    "English"
  ),
  new Question(
    "What does Fair Dinkum mean?",
    ["Honestly", "Most ", "Idiot", "Fraud"],
    "Honestly"
  ),
  new Question(
    "What does Arvo mean?",
    ["Avocado", "Afternoon", "Arrive", "Strong"],
    "Afternoon"
  ),
  new Question(
    "What does Brekky mean?",
    ["Sandwich", "Brick", "Breakfast", "Baseball"],
    "Breakfast"
  ),
  new Question(
    "What does Lappy mean?",
    ["Lap", "Laptop", "Long", "Lift"],
    "Laptop"
  ),
  new Question(
    "Who own the world’s largest tram network?",
    ["Victoria Trams", "Yarra Trams", "Metropolitan Trains", "V/Line"],
    "Yarra Trams"
  ),
  new Question(
    "Which card is used to travel around Melbourne?",
    ["Go Card", "Myki Card", "Money Card", "Oyster Card"],
    "Myki Card"
  ),
  new Question(
    "Which airport is Victoria’s major domestic and international gateway?",
    [
      "Avalon Airport",
      "Tullamarine Airport",
      "Moorabbin Airport ",
      "Essendon Airport"
    ],
    "Tullamarine Airport"
  ),
  new Question(
    "Which AFL team was the first to complete the Premiership runners-up hat-trick twice?",
    ["Richmond", "Fitzroy", "Melbourne", "Collingwood"],
    "Collingwood"
  ),
  new Question(
    "Which is the largest annual sporting event in the Southern Hemisphere?",
    ["Melbourne Cup", "Australia Open", "Cricket", "AFL"],
    "Australia Open"
  ),
  new Question(
    "The sporting event infamous as -the race that stops the nations-?",
    ["Melbourne Cup", "Sydney Cup", "Queensland Cup", "Victoria Cup"],
    "Melbourne Cup"
  ),
  new Question(
    "How long is the footy/football match?",
    ["30 minutes", "50 minutes", "60 minutes", "80 minutes"],
    "80 minutes"
  ),
  new Question(
    "How many team contests in the Australian Football League?",
    ["6", "10", "14", "18"],
    "18"
  ),
  new Question(
    "Adding this over meat while barbecue makes the meat more tender according to Australians?",
    ["Wine", "Beer", "Olive oil", "Walnut oil"],
    "Beer"
  ),
  new Question(
    "You can easily find coin-operated electric barbecue in public places?",
    ["True", "False"],
    "True"
  ),
  new Question(
    "You can easily find coin-operated electric barbecue in public places?",
    ["True", "Flase"],
    "True"
  ),
  new Question(
    "Roughly how many beaches are there in Australia?",
    ["1000", "4000", "8000", "11000"],
    "11000"
  ),
  new Question(
    "You will see many Australian having barbecue sessions at their home around this time of year?",
    ["Summer", "Spring", "Autumn", "All Seasons"],
    "All Seasons"
  )
];

// var url = window.location.pathname;
// console.log(url);
// console.log(url == "/quiz-language");
// console.log(questions.length);

if (window.location.pathname == "/quiz-language") {
  questions = questions.slice(0, 5);
}

if (window.location.pathname == "/quiz-transport") {
  questions = questions.slice(5, 8);
}
if (window.location.pathname == "/quiz-sport") {
  questions = questions.slice(8, 13);
}
if (window.location.pathname == "/quiz-culture") {
  questions = questions.slice(13, 18);
}

var quiz = new Quiz(questions);

function populate() {
  if (quiz.isEnded()) {
    showScores();
  } else {
    //show questions
    var element = document.getElementById("question");
    element.innerHTML = quiz.getQuestionIndex().text;

    // show choices
    var choices = quiz.getQuestionIndex().choices;
    for (var i = 0; i < choices.length; i++) {
      var element = document.getElementById("choice" + i);
      element.innerHTML = choices[i];
      guess("btn" + i, choices[i]);
    }
    showProgress();
  }
}

function showProgress() {
  var currentQuestionNumber = quiz.questionIndex + 1;
  var element = document.getElementById("progress");
  element.innerHTML =
    "Question " + currentQuestionNumber + " of " + quiz.questions.length;
}

function guess(id, guess) {
  var button = document.getElementById(id);
  button.onclick = function () {
    quiz.guess(guess);
    populate();
  };
}

function showScores() {
  var gameOverHtml = "<h1>Result</h>";
  gameOverHtml += "<h2 id='score'>Your scores: " + quiz.score + "</h2>";
  gameOverHtml += "<div><a id='exit_btn' href='learnmore' type='button' >Exit</a> </div>";
  var elemet = document.getElementById("quiz");
  elemet.innerHTML = gameOverHtml;
}
populate();
