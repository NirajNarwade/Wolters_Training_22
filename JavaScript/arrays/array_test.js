const charArray = ["a", "s", "d"];

function capitalize(char) {
  //   console.log(char.toUpperCase());
  //   console.log(char);
  return char.toUpperCase();
}

// capitalize("w");
// console.log(charArray.forEach(capitalize));
// const str = "javascript";
// console.log(testArr.forEach(capitalize));
//
// map function is an extension to this
// map takes an array as an input returns another array as output

// const newArray = charArray.map(capitalize);
// console.log(typeof newArray);
// console.log(newArray);

// charArray.filter(filterFunction);

const testStr = "javascript";
const testArr = [...testStr];

const vowelSet = new Set(["a", "e", "i", "o", "u"]);

function omitVowels(item) {
  if (vowelSet.has(item)) {
    console.log(`${item} is a vowel.`);
  } else {
    return item;
  }
}

const outArr = testArr.filter(omitVowels);
console.log(outArr);

function concat1(accumulator, item) {
  return accumulator + item;
}

const concat1Result = testArr.reduce(concat1);
console.log(concat1Result);
