let data = require('./data.json')

part1 = data.filter((datum, i, arr) => arr[i] > arr[i-1]).length

console.log(part1)