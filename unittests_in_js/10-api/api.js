const express = require('express');
const bodyParser = require('body-parser'); // Import du middleware Body Parser
const port = 7865;
const app = express();

app.use(bodyParser.json()); // Utilisation du middleware Body Parser pour parser les données JSON

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

app.get('/available_payments', (req, res) => {
    res.send(
        {
            payment_methods: {
                credit_cards: true,
                paypal: false
                }
        }
    )
});

app.post('/login', (req, res) => {
    const { userName } = req.body;
    if (userName) {
        res.send(`Welcome ${userName}`);
    } else {
        res.status(400);
        res.end();
    }
});

app.listen(port, () => {
    console.log(`API available on localhost port ${port}`);
});

module.exports = app;
