let someNumber = 5;
let otherNumber = undefined;

console.log(otherNumber);
//Bang bang! you're boolean!
console.log(!!otherNumber);
console.log(Boolean(otherNumber));

let var1 = 2;
let var2 = 6;

var2 = var1 !== undefined ? !!var1 : var2;

if (var1 !== undefined) {
  var2 = Boolean(var1);
}

console.log(var2);