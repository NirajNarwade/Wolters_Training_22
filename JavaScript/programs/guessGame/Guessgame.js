var randInt = NaN;
var trials = 0;
function buttonHandeler() {
  document.getElementById("btn1").style.display = "none";
  document.getElementById("btn3").style.display = "none";
  document.getElementById("div1").style.display = "block";
  getRandomInt();
}

function guess(num) {
  trials = trials + 1;
  document.getElementById("in1").value = "";
  document.getElementById("trials").innerHTML = "Trials :" + trials;
  if (randInt == num) {
    document.getElementById("p1").innerHTML =
      "Hurrayy! You Guessed correct Number :)\nYou took " +
      trials +
      " this time.";
    document.getElementById("btn2").style.display = "none";
    document.getElementById("btn3").style.display = "block";
    document.getElementById("p1").style.color = "brown";
  } else if (num < randInt) {
    document.getElementById("p1").innerHTML = "You are close! Guess Higher.";
    document.getElementById("p1").style.color = "green";
  } else if (num > randInt) {
    document.getElementById("p1").innerHTML = "You are close! Guess Lower.";
    document.getElementById("p1").style.color = "red";
  }
}

function getRandomInt() {
  randInt = Math.floor(Math.random() * (100 - 1 + 1) + 1);
  trials = 0;
  document.getElementById("trials").innerHTML = "Trials :" + trials;
  document.getElementById("p1").innerHTML = "Number is between 1 - 100";
  document.getElementById("btn2").style.display = "block";
  document.getElementById("btn3").style.display = "none";
}
