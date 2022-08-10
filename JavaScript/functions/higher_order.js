const convertToSingleWord = function (str) {
  console.log(str.replace(/ /g, "").toLowerCase());
};

// console.log(convertToSingleWord("Javascript drives me crazy."));

const convertFirstToUpper = function (str) {
  const [firstWord, ...otherWords] = str.split(" ");
  console.log(firstWord);
  console.log(otherWords);
  console.log([firstWord.toUpperCase(), ...otherWords].join(" "));
};

// convertFirstToUpper("Javascript drives me crazy.");

const transform = function (str, someFunction) {
  console.log(someFunction(str));
};

transform("Javascript drives me crazy.", convertToSingleWord);
document.querySelector("someelement").addEventListener("click", callBackFn);

// returning a function from another functions
