# Unittests in JS

### 0. Basic test with Mocha and Node assertion library

#### Task Description:
- Install Mocha using npm.
- Set up a script in your package.json to quickly run Mocha using npm test.
- Create a function named `calculateNumber` in a file named `0-calcul.js`.
- The `calculateNumber` function should accept two arguments `a` and `b`, both numbers.
- The function should round `a` and `b` and return the sum of the rounded values.
- Write test cases for this function in a file named `0-calcul.test.js`.
- Use the Node.js assert module for assertions.

#### Example Test Cases:
```javascript
const calculateNumber = require("./0-calcul.js");

calculateNumber(1, 3);      // Should return 4
calculateNumber(1, 3.7);    // Should return 5
calculateNumber(1.2, 3.7);  // Should return 5
calculateNumber(1.5, 3.7);  // Should return 6
```

#### Run Test:
```bash
npm test 0-calcul.test.js
```

### 1. Combining descriptions

#### Task Description:
- Upgrade the `calculateNumber` function to accept a third argument `type`.
- The `type` can be 'SUM', 'SUBTRACT', or 'DIVIDE'.
- When the `type` is 'SUM', round the numbers and add `a` to `b`.
- When the `type` is 'SUBTRACT', round the numbers and subtract `b` from `a`.
- When the `type` is 'DIVIDE', round the numbers and divide `a` by `b`.
- If `b` is 0 in case of division, return the string 'Error'.
- Write test cases for these functionalities.

#### Example Test Cases:
```javascript
const calculateNumber = require("./1-calcul.js");

calculateNumber('SUM', 1.4, 4.5);    // Should return 6
calculateNumber('SUBTRACT', 1.4, 4.5);   // Should return -4
calculateNumber('DIVIDE', 1.4, 4.5);   // Should return 0.2
calculateNumber('DIVIDE', 1.4, 0);   // Should return 'Error'
```

#### Run Test:
```bash
npm test 1-calcul.test.js
```

### 2. Basic test using Chai assertion library

#### Task Description:
- Rewrite the test suite using the Chai assertion library.
- Ensure that every test passes without any warnings.

#### Run Test:
```bash
npm test 2-calcul_chai.test.js
```

### 3. Spies

#### Task Description:
- Use Sinon to create a spy to verify the function calls and arguments.
- Spy on the function `Utils.calculateNumber` used inside the function `sendPaymentRequestToApi`.
- Ensure that every test passes without any warnings.

#### Run Test:
```bash
npm test 3-payment.test.js
```

### 4. Stubs

#### Task Description:
- Use Sinon to create a stub to replace the expensive function call.
- Stub the function `Utils.calculateNumber` to always return the same number (e.g., 10).
- Verify that the stub is being called with the correct arguments.
- Ensure that every test passes without any warnings.

#### Run Test:
```bash
npm test 4-payment.test.js
```

### 5. Hooks

#### Task Description:
- Use beforeEach and afterEach hooks to set up and clean up the environment.
- Ensure that the console is logging the correct message.
- Ensure that the console is only called once.
- Ensure that every test passes without any warnings.

#### Run Test:
```bash
npm test 5-payment.test.js
```

### 6. Async tests with done

#### Task Description:
- Write an async test using the `done` callback.
- Verify the result of an async function call with different parameters.
- Ensure that every test passes without any warnings.

#### Run Test:
```bash
npm test 6-payment_token.test.js
```

### 7. Skip

#### Task Description:
- Skip failing tests instead of commenting them out or removing them.
- Ensure that every test passes without any warnings.

#### Run Test:
```bash
npm test 7-skip.test.js
```

### 8. Basic Integration testing

#### Task Description:
- Perform basic integration testing on an API endpoint.
- Ensure that the correct response is returned for the index page.
- Ensure that every test passes without any warnings.

#### Run Test:
```bash
npm test 8-api/api.test.js
```

### 9. Regex integration testing

#### Task Description:
- Perform integration testing on API endpoints with regex validation.
- Ensure that the correct response and status code are returned for valid and invalid endpoints.
- Ensure that every test passes without any warnings.

#### Run Test:
```bash
npm test 9-api/api.test.js
```

### 10. Deep equality & Post integration testing

#### Task Description:
- Test API endpoints that return objects and handle POST requests.
- Ensure that the correct responses are returned for different scenarios.
- Ensure that every test passes without any warnings.

#### Run Test:
```bash
npm test 10-api/api.test.js
```

These tasks will help you practice writing unit tests, integration tests, and working with various testing libraries and tools in JavaScript. Let me know if you need further clarification on any task!