// var pname = NaN;
// var age = NaN;
// var gender = NaN;
// var number = NaN;

let patientList = [];
function addNew(){
    clearInputs();
    document.getElementById("patientform").style.display = "block";
    document.getElementById("patientlist").style.display = "none";
}

function viewAll(){
    document.getElementById("patientform").style.display = "none";
    document.getElementById("patientlist").style.display = "block";
    document.getElementById("list").innerHTML = "";
    patientList.forEach(showPatient);
}

let showPatient = function (p){
    document.getElementById("list").innerText += "Name : "+`${p.Name}`+"\nAge : "+`${p.Age}`+"\nGender : "+`${p.Gender}`+"\nContact Number : "+`${p.Number}`+"\n\n"; 
    
}

clearInputs = function () {
    let inputs = document.getElementsByTagName("input");
    for (let input of inputs) {
      if (input.getAttribute("type") != "button") input.value = "";
    }
  };


// function changeHandler(name,value){
//     console.log(name,value);
//     // name = value;
// }

function register(){
    let patient = {}
    patient.Name = document.getElementById("pname").value;
    patient.Age = document.getElementById("age").value;
    patient.Gender = document.getElementById("gender").value;
    patient.Number = document.getElementById("number").value;
    // console.log(patient);
    patientList.push(patient);
    // console.log(patientList);
    viewAll()
}

viewAll()