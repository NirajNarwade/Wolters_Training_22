let num_array = [1, 2, 8, 4, 10, 6, 7, 3, 9, 5];

let sqr_array = [];
let num_square = function (num) {
  sqr_array.push(num * num);
};
num_array.forEach(num_square);
// console.log(sqr_array);

let num_square_map = function (num) {
  return num * num;
};
// console.log(num_array.map(num_square_map));

let check_if_positive = function (x) {
  return x % 2 == 0;
};

// console.log(num_array.filter(check_if_positive));

const find_max = function (x, y) {
  return x > y ? x : y;
};

console.log(num_array.reduce(find_max));

// 1st call - [2, 8, 4, 10, 6, 7, 3, 9, 5]
// 1st call - [8, 4, 10, 6, 7, 3, 9, 5]
// 1st call - [8, 10, 6, 7, 3, 9, 5]