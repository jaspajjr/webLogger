const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.sendFile('/home/dom/code/webLogger/webLogger/templates/layout.html')
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})
