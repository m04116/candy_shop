const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');

const { getBit } = require('./bitfinex');

const app = express();

const rootPath = path.resolve('./app');

const viewsPath = path.resolve(rootPath, 'views');
const staticPath = path.resolve(rootPath, 'public');

app.set('views', viewsPath);
app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.static(staticPath));

app.get('/', (req, res, next) => {
    res.render('index');
});

app.get('/price', (req, res) => {
    getBit()
        .then((response) => {
            const data = response.data ? response.data : {};
            res.json(data);
        })
        .catch((err) => {
            console.error(err.message);
        });
});

module.exports = app;