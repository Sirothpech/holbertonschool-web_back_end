# ES6 Basics

This repository contains JavaScript exercises that cover various ES6 (ECMAScript 2015) concepts. Each exercise focuses on a specific ES6 feature and provides a task to complete.

## Tasks

### Task 0: Const or let?

In this task, you'll modify the `taskFirst` function to instantiate variables using `const` and the `taskNext` function to instantiate variables using `let`. These functions demonstrate the use of `const` and `let` for variable declarations in ES6.

**Execution Example:**

```bash
$ npm run dev 0-main.js
I prefer const when I can. But sometimes let is okay
```

### Task 1: Block Scope

You need to modify the variables inside the `taskBlock` function so that the variables aren't overwritten inside the conditional block. This task illustrates the concept of block scope in ES6.

**Execution Example:**

```bash
$ npm run dev 1-main.js
[ false, true ]
[ false, true ]
```

### Task 2: Arrow functions

Rewrite the `addNeighborhood` function using ES6 arrow syntax. This task demonstrates the use of arrow functions to simplify function declarations.

**Execution Example:**

```bash
$ npm run dev 2-main.js
[ 'SOMA', 'Union Square', 'Noe Valley' ]
```

### Task 3: Parameter defaults

Condense the `getSumOfHoods` function to one line using default parameter values. This task showcases how to use default parameter values to simplify function logic.

**Execution Example:**

```bash
$ npm run dev 3-main.js
142
56
41
```

### Task 4: Rest parameter syntax for functions

Modify the `returnHowManyArguments` function to return the number of arguments passed to it using the rest parameter syntax. This task demonstrates how to use the rest parameter syntax in ES6 functions.

**Execution Example:**

```bash
$ npm run dev 4-main.js
1
4
```

### Task 5: The wonders of spread syntax

Using spread syntax, concatenate two arrays and each character of a string. This task illustrates the power of spread syntax in combining arrays and strings.

**Execution Example:**

```bash
$ npm run dev 5-main.js
[
  'a', 'b', 'c',
  'd', 'H', 'e',
  'l', 'l', 'o'
]
```

### Task 6: Take advantage of template literals

Rewrite the return statement in the `getSanFranciscoDescription` function using template literals to substitute variables. This task demonstrates the use of template literals in ES6.

**Execution Example:**

```bash
$ npm run dev 6-main.js
As of 2017, it was the seventh-highest income county in the United States, with a per capita personal income of $119,868. As of 2015, San Francisco proper had a GDP of $154.2 billion, and a GDP per capita of $178,479.
```

### Task 7: Object property value shorthand syntax

Modify the `getBudgetObject` function to use ES6 object property value shorthand syntax. This task showcases the shorthand syntax for object property assignment.

**Execution Example:**

```bash
$ npm run dev 7-main.js
{ income: 400, gdp: 700, capita: 900 }
```

### Task 8: No need to create empty objects before adding in properties

Rewrite the `getBudgetForCurrentYear` function to use ES6 computed property names on the budget object. This task demonstrates how to use computed property names in ES6.

**Execution Example:**

```bash
$ npm run dev 8-main.js
{ 'income-2021': 2100, 'gdp-2021': 5200, 'capita-2021': 1090 }
```

### Task 9: ES6 method properties

Rewrite the `getFullBudgetObject` function to use ES6 method properties in the `fullBudget` object. This task illustrates the use of ES6 method properties in objects.

**Execution Example:**

```bash
$ npm run dev 9-main.js
$20
20 euros
```

### Task 10: For...of Loops

Rewrite the `appendToEachArrayValue` function to use ES6's `for...of` operator and avoid using `var`. This task demonstrates how to use `for...of` loops in ES6.

**Execution Example:**

```bash
$ npm run dev 10-main.js
[ 'correctly-appended', 'correctly-fixed', 'correctly-displayed' ]
```

### Task 11: Iterator

Create a function named `createEmployeesObject` that returns an object mapping department names to arrays of employees. This task demonstrates object creation and manipulation in ES6.

**Execution Example:**

```bash
$ npm run dev 11-main.js
{ Software: [ 'Bob', 'Sylvie' ] }
```

### Task 12: Let's create a report object

Write a function named `createReportObject` that returns an object containing department names and a method to get the number of departments. This task combines previously learned concepts to create a report object.

**Execution Example:**

```bash
$ npm run dev 12-main.js
{ engineering: [ 'Bob', 'Jane' ], marketing: [ 'Sylvie' ] }
2
```

Each task folder contains a JavaScript file (e.g., `0-constants.js`) that you can modify to complete the task, and a `main.js` file (e.g., `0-main.js`) that demonstrates the task's execution. To run a specific task, use `npm run dev` followed by the task's main file (e.g., `npm run dev 0-main.js`). Enjoy learning and practicing ES6 features!
