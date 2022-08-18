// hoisting lets you access information before even declaration because of execution context
getfnc();
console.log(x);

function getfnc(){
    console.log("Hii Welcome!");
}

var x = 7;
// console.log("hiiiiiiiiiiiiiiiiiii");

console.log(getfnc);