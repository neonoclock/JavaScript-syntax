const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split(" ")

let a = Number(input[0])
let b = Number(input[1])
let c = Number(input[2])

if ((a > b && a < c) || (a > c && a < b)) {
    console.log(a);      // a가 중간
} 
else if ((b > a && b < c) || (b > c && b < a)) {
    console.log(b);      // b가 중간
} 
else {
    console.log(c);      // c가 중간
}