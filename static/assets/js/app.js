var questions = [
  new Question(
    "Which one is not correct1",
    ["Java", "C", "Haskell", "javascript"],
    "Haskell"
  ),
  new Question(
    "Which one is not correct2",
    ["Java", "C", "Haskell", "javascript"],
    "Java"
  ),
  new Question(
    "Which one is not correct3",
    ["Java", "C", "Haskell", "javascript"],
    "C"
  ),
  new Question(
    "Which one is not correct4",
    ["Java", "All", "Haskell", "javascript"],
    "All"
  ),
  new Question(
    "Which one is not correct5",
    ["MVC", "C", "Haskell", "javascript"],
    "MVC"
  )
];

questions = questions.slice(2, 5);
var url = window.location.pathname;
console.log(url);
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
  button.onclick = function() {
    quiz.guess(guess);
    populate();
  };
}

function showScores() {
  var gameOverHtml = "<h1>Result</h>";
  gameOverHtml += "<h2 id='score'>Your scores: " + quiz.score + "</h2>";
  var elemet = document.getElementById("quiz");
  elemet.innerHTML = gameOverHtml;
}
populate();
