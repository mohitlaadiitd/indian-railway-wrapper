const express = require('express');
const { spawn } = require('child_process');
const app = express();
const port = 3000;

const bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// use cors to allow cross origin resource sharing
const cors = require('cors');
app.use(cors());

app.get('/', (req, res) => {
    // run the python script and wait for it to finish
    console.log("Namaste Paaji")
});

app.post('/api', (req, res) => {
    // run the python script and wait for it to finish
    const body = req.body;
    console.log(body);
    const python = spawn('python3', ['src/scripts/combine.py', body['date'], body['source'], body['destination']]);
    python.stdout.on('data', function(data) {
        dataToSend = data.toString()
        console.log(dataToSend);
        res.json(JSON.parse(dataToSend));
    });
})

app.listen(port, () => console.log(`Break my Rail App listening on port ${port}!`));