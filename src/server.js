const { app, publicDirectoryPath } = require('./app');


app.listen(3000, () => {
    console.log('App running on port 3000...');
});

app.get('/', (req, res) => {
    res.status(200).sendFile(publicDirectoryPath + '/html/index.html')
});
