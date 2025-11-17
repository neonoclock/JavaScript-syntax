const fs = require("fs")
let N = Number(fs.readFileSync(0).toString().trim())

if ((N%3==0 && N%2==1) || (N%5==0 && N%2==0)) {
    console.log('true')
} else {
    console.log('false')
}