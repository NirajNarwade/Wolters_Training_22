class Person {
  #age;
  constructor(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  calcYOB() {
    return 2022 - this.#age;
  }

  setAge(age) {
    this.#age = age;
  }

  get name() {
    return `${this.firstName} ${this.lastName}`;
  }

  set age(age) {
    this.#age = age;
  }
}

const p1 = new Person("Niraj", "Narwade", 27);
// p1.#age = 90;
p1.setAge(30);
console.log(p1.calcYOB());
p1.age = 25;
console.log(p1.calcYOB());
// // p1.greet(p1.firstName);
console.log(p1.name);

console.log(p1);
// console.log(p1.__proto__);
// console.log(Person.prototype);
// console.log(p1.__proto__ === Person.prototype);
