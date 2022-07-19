// function add(val){
//     document.getElementById("in2").value += val
// }

// function process(val){

//     document.getElementById("in1").value = document.getElementById("in2").value+val
//     document.getElementById("in2").value = ""
// }
// function calculate(){

//     document.getElementById("in1").value += document.getElementById("in2").value

// }
// This function clear all the values
function clearScreen() {
  document.getElementById("result").value = "";
}

// This function display values
function display(value) {
  document.getElementById("result").value += value;
}

// This function evaluates the expression and returns result
function calculate() {
  var p = document.getElementById("result").value;
  var q = eval(p);
  document.getElementById("result").value = q;
}
