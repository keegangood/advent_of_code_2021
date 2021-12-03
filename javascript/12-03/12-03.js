let diagnosticReport = require('./data.json')

// create array of 0s to count occurances of 1s in diag report
let counts = Array(diagnosticReport[0].length).fill(0)

row = 0
while (row < diagnosticReport.length) {
  col = 0
  while (col < diagnosticReport[row].length) {
    // increase the count for current 'col' position if a '1' exists
    if (diagnosticReport[row][col] === '1') {
      counts[col]++
    }
    col++
  }
  row++
}

// replace each value with 1 if the count was greater than
// half of the length of the diagnostic report otherwise 0
gamma = counts.map(count =>
  count > Math.floor(diagnosticReport.length / 2) ? 1 : 0
)

// invert gamma digits to form epsilon array
epsilon = gamma.map(digit => (digit ? 0 : 1))


gamma = gamma.reduce((x, _, index, arr) => {
  let exponent = arr.length - (index + 1)
  return x + arr[index] * 2 ** exponent
}, 0)
epsilon = epsilon.reduce((x, _, index, arr) => {
  let exponent = arr.length - (index + 1)
  return x + arr[index] * 2 ** exponent
}, 0)

console.log(gamma * epsilon)
