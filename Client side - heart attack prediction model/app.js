const express = require('express')
const app = express();
var server = require('http').createServer(app);
const port = 6064;

app.use(express.static('public'))
app.set('view engine', 'ejs')

app.get('/', (req, res) => {
    res.render("frontend")
  })

  server.listen(port, () => console.log(`Listening Socket on http://localhost:6064`));