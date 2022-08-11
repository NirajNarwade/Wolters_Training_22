var randInt = NaN;
var randInt1 = NaN;
var round = 0;
var comp = 0;
var user = 0;
var tie = 0;
var choice1;
var choice2;
function buttonHandeler() {
  document.getElementById("btn1").style.display = "none"; 
  document.getElementById("div1").style.display = "block";
  // document.getElementsByClassName("box").style.WIDTH = "75%";
  document.getElementById("box").setAttribute("style","width: 75%");
  display()
}

function manual(){
  document.getElementById("div2").style.display = "block";
  document.getElementById("div3").style.display = "none";
}

function auto(){
  document.getElementById("div2").style.display = "none";
  document.getElementById("div3").style.display = "block";
  
}

function autoGame(){
  randInt1 = getRandomInt()
  game(randInt1)
}

function reset(){
  round = 0;
  comp = 0;
  user = 0;
  tie = 0;
  document.getElementById("choice").innerHTML = ""
  document.getElementById("choice1").innerHTML = ""
  display()
  info()
}

function check(ch2) {
  
  // alert(ch2)
  if(ch2!=1 & ch2!=2 & ch2!=3){
    document.getElementById("error").innerHTML = "Please, Enter correct input!"
    document.getElementById("error").style.color = "darkred";
    document.getElementById("choice").innerHTML = ""
    document.getElementById("in1").value = ""
    info()
  }else{
    game(ch2)
  }
}

function choice(){
  document.getElementById("choice").innerHTML = "Computer Chose: "+choice1+"<br/>You Chose: "+choice2
  document.getElementById("choice1").innerHTML = "Computer Chose: "+choice1+"<br/>You Chose: "+choice2
}

function selection(ch){
  if(ch == 1){
    return "Rock"
  }else if(ch == 2){
    return "Paper"
  }else{
    return "Scissor"
  }

}

function game(ch2){
  document.getElementById("error").innerHTML = ""  
  round = round + 1;
  ch1 = getRandomInt()
  choice1 = selection(ch1)
  choice2 = selection(ch2)
  choice()
  if (ch1 == ch2){
    tie+=1
    document.getElementById("p1").innerHTML = "Oops! It's a tie...Try again" 
    document.getElementById("p2").innerHTML = "Oops! It's a tie...Try again" 
    document.getElementById("p1").style.color = "brown";
    document.getElementById("p2").style.color = "brown";
  }else{
    if(ch1 == 1){
      if(ch2 == 2){
        user+=1
        document.getElementById("p1").innerHTML = "Hurrayyy! You won the round!!!" 
        document.getElementById("p2").innerHTML = "Hurrayyy! You won the round!!!" 
        document.getElementById("p1").style.color = "green";
        document.getElementById("p2").style.color = "green";
      }else{
        comp+=1
        document.getElementById("p1").innerHTML = "Damn it! Computer won the round." 
        document.getElementById("p2").innerHTML = "Damn it! Computer won the round." 
        document.getElementById("p1").style.color = "darkred";
        document.getElementById("p2").style.color = "darkred";
      }
    }else if(ch1 ==2){
      if(ch2 == 3){
        user+=1
        document.getElementById("p1").innerHTML = "Hurrayyy! You won the round!!!" 
        document.getElementById("p2").innerHTML = "Hurrayyy! You won the round!!!" 
        document.getElementById("p1").style.color = "green";
        document.getElementById("p2").style.color = "green";
      }else{
        comp+=1
        document.getElementById("p1").innerHTML = "Damn it! Computer won the round." 
        document.getElementById("p2").innerHTML = "Damn it! Computer won the round." 
        document.getElementById("p1").style.color = "darkred";
        document.getElementById("p2").style.color = "darkred";
      }
    }else if(ch1 ==3){
      if(ch2 == 1){
        user+=1
        document.getElementById("p1").innerHTML = "Hurrayyy! You won the round!!!" 
        document.getElementById("p2").innerHTML = "Hurrayyy! You won the round!!!" 
        document.getElementById("p1").style.color = "green";
        document.getElementById("p2").style.color = "green";
      }else{
        comp+=1
        document.getElementById("p1").innerHTML = "Damn it! Computer won the round."
        document.getElementById("p2").innerHTML = "Damn it! Computer won the round."
        document.getElementById("p1").style.color = "darkred"; 
        document.getElementById("p2").style.color = "darkred"; 
        
      }
    }
  }
  display()
  document.getElementById("in1").value = ""
}

function getRandomInt() {
    return Math.floor(Math.random() * (3 - 1 + 1) + 1);
}

function display(){
  document.getElementById("round").innerHTML = round;
  document.getElementById("comp").innerHTML = comp;
  document.getElementById("you").innerHTML = user;
  document.getElementById("tie").innerHTML = tie;
}

function info(){
  document.getElementById("p1").innerHTML = "Computer has made it's choice. Now its your turn";
  document.getElementById("p1").style.color = "white";
  document.getElementById("p2").innerHTML = "Let's Go!";
  document.getElementById("p2").style.color = "white";
 
}
