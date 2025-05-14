var realString = 'hello!';
var emptyString = '';

var nullString = null;
var undefinedString = undefined;

if (Boolean(realString)) {
  console.log(realString);
} else {
  console.log('Nothing here!');
}

if (emptyString === '') {
  console.log('empty string!');
}
