function toLower(word) {
  return word.toLowerCase();
}

const words = ['Hello', 'World', 'foo', 'bar'];

const lowerWords = words.map(x => x.toLowerCase());

console.log(lowerWords);