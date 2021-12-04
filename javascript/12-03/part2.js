let diagnosticReport = require('./data.json')

const toDecimal = binary =>
  [...binary].reduce((x, _, index, arr) => {
    let exponent = arr.length - (index + 1)
    return x + arr[index] * 2 ** exponent
  }, 0)

const getDigitCounts = data => {
  // create array of 0s to count occurances of 1s in diag report
  let ones = Array(data[0].length).fill(0)

  row = 0
  while (row < data.length) {
    col = 0
    while (col < data[row].length) {
      // increase the count for current 'col' position if a '1' exists
      if (data[row][col] === '1') {
        ones[col]++
      }
      col++
    }
    row++
  }

  zeros = ones.map(one => data.length - one)

  return [zeros, ones]
}

const findRating = (data, criteria) => {
  let prefix = ''

  while (data.length > 1) {
    let [zeros, ones] = getDigitCounts(data)
    let index = prefix.length

    criteria === 'high'
      ? (prefix += zeros[index] > ones[index] ? '0' : '1')
      : (prefix += zeros[index] <= ones[index] ? '0' : '1')

    data = data.filter(row => row.startsWith(prefix))
  }

  return data[0]
}

const O2 = toDecimal(findRating(diagnosticReport, 'high'))
const CO2 = toDecimal(findRating(diagnosticReport, 'low'))

console.log(O2 * CO2) // 587895
