const fs = require("fs");
let [a, b, c] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

if ((a > b && a < c) || (a > c && a < b)) {
    console.log(a);      // a가 중간
} 
else if ((b > a && b < c) || (b > c && b < a)) {
    console.log(b);      // b가 중간
} 
else {
    console.log(c);      // c가 중간
}