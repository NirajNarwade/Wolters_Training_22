const question = new Map([
  ["Niraj", 100],
  ["Simba", 101],
  [102, "Karan"],
  [true, "back to office"],
  [
    [1, 2],
    ["hello", "world"],
  ],
]);
// console.log(question.get(""));
let key_itr = question.keys();
console.log(question.get(key_itr.next().value));
console.log(question.get(key_itr.next().value));
console.log(question.get(key_itr.next().value));
console.log(question.get(key_itr.next().value));
// console.log(question.get(key_itr.next().value));
// console.log(question.get(key_itr.next().value));
// let last_key = key_itr.next().value;
let last_key = [1, 2];
console.log(typeof last_key);
console.log(question.get(last_key));

