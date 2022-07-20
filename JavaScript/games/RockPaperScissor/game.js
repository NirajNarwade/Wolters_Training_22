var randInt = NaN;
var round = 0;
var comp = 0;
var user = 0;
function buttonHandeler() {
  document.getElementById("btn1").style.display = "none"; 
  document.getElementById("div1").style.display = "block";
}

function check(ch2) {
  round = round + 1;
  ch1 = getRandomInt()
//   document.getElementById("in1").value = "";
//   document.getElementById("round").innerHTML = "round :" + round;
//   if (randInt == num) {
//     document.getElementById("p1").innerHTML =
//       "Hurrayy! You Guessed correct Number :)\nYou took " +
//       round +
//       " this time.";
//     document.getElementById("btn2").style.display = "none";
//     document.getElementById("btn3").style.display = "block";
//     document.getElementById("p1").style.color = "brown";
//   } else if (num < randInt) {
//     document.getElementById("p1").innerHTML = "You are close! Guess Higher.";
//     document.getElementById("p1").style.color = "green";
//   } else if (num > randInt) {
//     document.getElementById("p1").innerHTML = "You are close! Guess Lower.";
//     document.getElementById("p1").style.color = "red";
//   }
}

function getRandomInt() {
    document.getElementById("round").innerHTML = round;
    document.getElementById("comp").innerHTML = comp;
    document.getElementById("you").innerHTML = user;
    document.getElementById("p1").innerHTML = "Computer has chosen";
    return Math.floor(Math.random() * (3 - 1 + 1) + 1);
}
