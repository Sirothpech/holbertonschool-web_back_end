# ES6 Promises

This repository contains JavaScript code examples related to Promises in ES6.

## Table of Contents

1. [Keep every promise you make and only make promises you can keep](#keep-every-promise-you-make-and-only-make-promises-you-can-keep)
2. [Don't make a promise...if you know you can't keep it](#dont-make-a-promiseif-you-know-you-cant-keep-it)
3. [Catch me if you can!](#catch-me-if-you-can)
4. [Handle multiple successful promises](#handle-multiple-successful-promises)
5. [Simple promise](#simple-promise)
6. [Reject the promises](#reject-the-promises)
7. [Handle multiple promises](#handle-multiple-promises)
8. [Load balancer](#load-balancer)
9. [Throw error / try catch](#throw-error--try-catch)
10. [Throw an error](#throw-an-error)

---

### 1. Keep every promise you make and only make promises you can keep

**File**: `0-promise.js`

```javascript
import getResponseFromAPI from "./0-promise.js";

const response = getResponseFromAPI();
console.log(response instanceof Promise);
```

**Expected Output:**

```
true
```

---

### 2. Don't make a promise...if you know you can't keep it

**File**: `1-promise.js`

```javascript
import getFullResponseFromAPI from './1-promise';

console.log(getFullResponseFromAPI(true));
console.log(getFullResponseFromAPI(false));
```

**Expected Output:**

```
Promise { { status: 200, body: 'Success' } }
Promise {
  <rejected> Error: The fake API is not working currently
    ...
    ...
```

---

### 3. Catch me if you can!

**File**: `2-then.js`

```javascript
import handleResponseFromAPI from "./2-then";

const promise = Promise.resolve();
handleResponseFromAPI(promise);
```

**Expected Output:**

```
Got a response from the API
```

---

### 4. Handle multiple successful promises

**File**: `3-all.js`

```javascript
import handleProfileSignup from "./3-all";

handleProfileSignup();
```

**Expected Output:**

```
photo-profile-1 Guillaume Salva
```

---

### 5. Simple promise

**File**: `4-user-promise.js`

```javascript
import signUpUser from "./4-user-promise";

console.log(signUpUser("Bob", "Dylan"));
```

**Expected Output:**

```
Promise { { firstName: 'Bob', lastName: 'Dylan' } }
```

---

### 6. Reject the promises

**File**: `5-photo-reject.js`

```javascript
import uploadPhoto from './5-photo-reject';

console.log(uploadPhoto('guillaume.jpg'));
```

**Expected Output:**

```
Promise {
  <rejected> Error: guillaume.jpg cannot be processed
  ..
    ..
```

---

### 7. Handle multiple promises

**File**: `6-final-user.js`

```javascript
import handleProfileSignup from './6-final-user';

console.log(handleProfileSignup("Bob", "Dylan", "bob_dylan.jpg"));
```

**Expected Output:**

```
Promise { <pending> }
```

---

### 8. Load balancer

**File**: `7-load_balancer.js`

```javascript
import loadBalancer from "./7-load_balancer";

const ukSuccess = 'Downloading from UK is faster';
const frSuccess = 'Downloading from FR is faster';

const promiseUK = new Promise(function(resolve, reject) {
    setTimeout(resolve, 100, ukSuccess);
});

const promiseUKSlow = new Promise(function(resolve, reject) {
    setTimeout(resolve, 400, ukSuccess);
});

const promiseFR = new Promise(function(resolve, reject) {
    setTimeout(resolve, 200, frSuccess);
});

const test = async () => {
    console.log(await loadBalancer(promiseUK, promiseFR));
    console.log(await loadBalancer(promiseUKSlow, promiseFR));
}

test();
```

**Expected Output:**

```
Downloading from UK is faster
Downloading from FR is faster
```

---

### 9. Throw error / try catch

**File**: `8-try.js`

```javascript
import divideFunction from './8-try';

console.log(divideFunction(10, 2));
console.log(divideFunction(10, 0));
```

**Expected Output:**

```
5
..../8-try.js:15
  throw Error('cannot divide by 0');
  ^
.....
```

---

### 10. Throw an error

**File**: `9-try.js`

```javascript
import guardrail from './9-try';
import divideFunction from './8-try';

console.log(guardrail(() => { return divideFunction(10, 2)}));
console.log(guardrail(() => { return divideFunction(10, 0)}));
```

**Expected Output:**

```
[ 5, 'Guardrail was processed' ]
[ 'Error: cannot divide by 0', 'Guardrail was processed' ]
```

---

Feel free to explore and test these code examples to understand how Promises work in ES6. Each example provides a practical use case for working with Promises in JavaScript.
