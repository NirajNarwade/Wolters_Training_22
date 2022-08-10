const listOfStudents = ["Niraj", "Simba", "Rajani", "Vinayak"];
const setofStudents = new Set(listOfStudents);
// console.log(listOfStudents);
// console.log(setofStudents);

// const nums = new Set();
// nums.add(1);
// console.log(nums);
// // set size
// console.log(setofStudents.size);

// // checking membership
// console.log(setofStudents.has("Simba"));

// adding and deleting elements
// setofStudents.add("Jayashri");
// setofStudents.delete("Niraj");
// console.log(setofStudents);

// setofStudents.clear();
// console.log(setofStudents);

// looping over a set
// for (let student of setofStudents) console.log(student);

// set iterator
let itr = setofStudents.values();

console.log(itr.next().value);
console.log(itr.next().value);
console.log(itr.next().value);
console.log(itr.next().value);

// function display(item) {
//   console.log(item);
// }

// // for (let student of setofStudents) display(student);

// setofStudents.forEach(display);

// display("some string");
// setofStudents.forEach(display);
