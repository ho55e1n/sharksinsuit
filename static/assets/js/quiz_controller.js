function Quiz(questions) {
  this.score = 0;
  this.questions = questions;
  this.questionIndex = 0;
  this.wronganswers = []
}

Quiz.prototype.getQuestionIndex = function () {
  return this.questions[this.questionIndex];
};

Quiz.prototype.isEnded = function () {
  return this.questions.length === this.questionIndex;
};
Quiz.prototype.guess = function (answer) {
  if (this.getQuestionIndex().correctAnswer(answer)) {
    this.score++;
  } else {
    console.log("inside the else ")
    console.log(this.questionIndex)
    var wronganswertext = "<br />" + (this.questionIndex + 1) + " - " + answer + " &#10060; " + this.getQuestionIndex().answer + " &#9989;" + "<br />"
    console.log("inside prototype gusee " + wronganswertext)
    this.wronganswers.push(wronganswertext)
    // this.wronganswers.push(this.getQuestionIndex().answer)
    // this.wronganswers.push("&#10062;")
  }
  this.questionIndex++;
};
