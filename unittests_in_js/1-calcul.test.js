const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
    it('test', () => {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        assert.strictEqual(calculateNumber('SUM', 1.4, -4.5), -3);
        assert.strictEqual(calculateNumber('SUBSTRACT', 1.4, 4.5), -4);
        assert.strictEqual(calculateNumber('SUBSTRACT', 2, 2), 0);
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
});
