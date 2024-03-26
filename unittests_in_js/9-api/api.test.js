const chai = require('chai');
const request = require('request');
const { expect } = chai;

describe('Index page', () => {
    const url = 'http://localhost:7865/';

    it('should return status code 200 for the index page', (done) => {
        request(url, (error, response, body) => {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('should return "Welcome to the payment system" for the index page', (done) => {
        request(url, (error, response, body) => {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
});

describe('Cart page', () => {
    const baseUrl = 'http://localhost:7865';

    it('should return payment methods when cart id is a number', (done) => {
        const cartId = 12;
        const url = `${baseUrl}/cart/${cartId}`;
        request(url, (error, response, body) => {
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal(`Payment methods for cart ${cartId}`);
            done();
        });
    });

    it('should return 404 status code when cart id is not a number', (done) => {
        const cartId = 'hello';
        const url = `${baseUrl}/cart/${cartId}`;
        request(url, (error, response, body) => {
            expect(response.statusCode).to.equal(404);
            done();
        });
    });
});
