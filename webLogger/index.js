const express = require('express')
const app = express()

app.get('/', function (req, res) {
  var file_path = "/templates/layout.html"
  var fullpath = __dirname + file_path;
  res.sendFile(fullpath)
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})
