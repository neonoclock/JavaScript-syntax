const fs = require("fs")
let N = Number(fs.readFileSync(0).toString().trim());

let result = ""

for (let i=N; i<=N*5 ; i+=N) {
    result += i + " ";
}

console.log(result);