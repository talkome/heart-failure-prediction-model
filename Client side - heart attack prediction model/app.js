const express = require('express')
const app = express();
var server = require('http').createServer(app);
const port = process.env.PORT || 8080;

app.use(express.static('public'))
app.set('view engine', 'ejs')

app.get('/', (req, res) => {
    res.render("frontend")
  })

  server.listen(port, () => console.log(`Listening...`));