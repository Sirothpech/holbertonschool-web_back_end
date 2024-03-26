const sinon = require('sinon');
const assert = require('assert');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
    let consoleLogStub;

    beforeEach(() => {
        // Crée un stub pour console.log
        consoleLogStub = sinon.stub(console, 'log');
    });

    afterEach(() => {
        // Restaure le stub après chaque test
        consoleLogStub.restore();
    });

    it('should log the correct message for total amount of 100 and total shipping of 20', () => {
        // Appelle la fonction à tester
        sendPaymentRequestToApi(100, 20);

        // Vérifie que Utils.calculateNumber a été appelé avec les bons arguments
        sinon.assert.calledOnceWithExactly(consoleLogStub, 'The total is: 120');
    });

    it('should log the correct message for total amount of 100 and total shipping of 10', () => {
        // Appelle la fonction à tester
        sendPaymentRequestToApi(10, 10);

        // Vérifie que Utils.calculateNumber a été appelé avec les bons arguments
        sinon.assert.calledOnceWithExactly(consoleLogStub, 'The total is: 20');
    });
});
