
class Person {
  constructor(firstName, lastName, yearOfBirth) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.yearOfBirth = yearOfBirth;
  }

  // instead of manually adding the methods to the prototype, we can add them directly to the class
  calcAge() {
    return 2022 - this.yearOfBirth;
  }
}

const p1 = new Person("Niraj", "Narwade", 1977);

console.log(p1);
console.log(p1.calcAge());
console.log(p1.__proto__);
console.log(Person.prototype);
console.log(p1.__proto__ === Person.prototype);

// we can also add methods at a later time directly to the prototype object
// Person.prototype.greet = function () {
//   console.log(`Hello ${this.firstName}`);
// };
p1.greet();

// not allowed
Person.greet = function () {
  console.log(`Hello ${this.firstName}`);
};
Person.greet();
