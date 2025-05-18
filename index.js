const express = require('express');
require('dotenv').config();
const bodyParser = require('body-parser');

const app = express();

const PORT = process.env.PORT || 4000;

app.use(express.json());

app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.listen(PORT, () => {
    console.log(`Server running on PORT ${PORT}`);
});