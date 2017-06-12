const express = require('express')
const app = express()
const cookieParser = require('cookie-parser');

app.use(cookieParser());

app.get('/', function (req, res) {
  let file_path = "/templates/layout.html"
  let fullpath = __dirname + file_path;

  res.cookie(cookie_name , 'cookie_value').sendFile(fullpath)
  console.log(req.headers)
})

app.listen(3000, function (req, res) {
  console.log('Example app listening on port 3000!')
})
