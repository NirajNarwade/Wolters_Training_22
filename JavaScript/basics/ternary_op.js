var empType = "permanent";
var salType = empType === "permanent" ? "salary" : "stipend";
console.log(salType);

function someFunction() {
  var fnVar = "hi";
  console.log(empType);
}

someFunction();
console.log(fnVar);
