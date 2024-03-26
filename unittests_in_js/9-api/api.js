const express = require('express');
const port = 7865;
const app = express();

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

app.get('/cart/:id(\\d+)', (req, res) => {
    const cartId = req.params.id;
    if (!isNaN(cartId)) {
        res.send(`Payment methods for cart ${cartId}`);
    } else {
        res.status(400).send('Invalid cart ID. Please provide a valid numeric ID.');
    }
});

app.listen(port, () => {
    console.log(`API available on localhost port ${port}`);
});

module.exports = app;
