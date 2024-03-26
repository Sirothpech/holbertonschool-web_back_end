const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
    it('test', () => {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        assert.strictEqual(calculateNumber('SUM', 1.4, -4.5), -3);
        assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        assert.strictEqual(calculateNumber('SUBTRACT', 2, 2), 0);
        assert.strictEqual(calculateNumber('SUBTRACT', 2.7, 2), 1);
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        assert.strictEqual(calculateNumber('DIVIDE', -3, 1.2), -3);
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
});
