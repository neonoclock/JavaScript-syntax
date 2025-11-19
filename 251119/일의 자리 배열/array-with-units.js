const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split(" ")

let a = Number(input[0])
let b = Number(input[1])

let result = []

result.push(a)
result.push(b)

for (let i=2; i<10; i++) {
    result[i] = (result[i-1] + result[i-2]) % 10
}

console.log(result.join(" "))