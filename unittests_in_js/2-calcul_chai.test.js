const chai = require('chai');
const { expect } = chai;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
    it('test', () => {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
        expect(calculateNumber('SUM', 1.4, -4.5)).to.equal(-3);
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
        expect(calculateNumber('SUBTRACT', 2, 2)).to.equal(0);
        expect(calculateNumber('SUBTRACT', 2.7, 2)).to.equal(1);
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
        expect(calculateNumber('DIVIDE', -3, 1.2)).to.equal(-3);
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
        expect(calculateNumber('DIVIDE', 1.4, 0.2)).to.equal('Error');
    });
});
