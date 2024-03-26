const sinon = require('sinon');
const assert = require('assert');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
    it('should call Utils.calculateNumber with correct arguments', () => {
        const calculateNumberSpy = sinon.stub(Utils, 'calculateNumber').returns(10);
        const consoleLogSpy = sinon.stub(console, 'log')
        sendPaymentRequestToApi(100, 20);
        sinon.assert.calledOnce(calculateNumberSpy);
        sinon.assert.calledWithExactly(calculateNumberSpy, 'SUM', 100, 20);
        sinon.assert.calledOnceWithExactly(consoleLogSpy, 'The total is: 10');

        calculateNumberSpy.restore(); // Restaure le spy pour éviter les effets de bord
        consoleLogSpy.restore();
    });
});
