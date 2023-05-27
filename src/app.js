const express = require('express');
const path = require('path');

const app = express();

app.set('view engine', 'ejs');
app.set('views', __dirname + '/public/html/');

const publicDirectoryPath = path.join(__dirname, '..', 'public');

module.exports = {
    app, 
    publicDirectoryPath
};