const words = ['Hello', 'World', 'foo', 'bar'];

function toLower(word) {
  return word.toLowerCase();
}

const lowerWords2 = words.map(toLower);
const lowerWords = words.map(x => x.toLowerCase());

console.log(words);
console.log(lowerWords);
console.log(lowerWords2);