# ES6 Classes

This project involves implementing several classes and exploring the concepts of object-oriented programming using ES6 classes in JavaScript.

## 0. You used to attend a place like this at some point

In this task, we create a class called `ClassRoom` with a constructor that accepts a `maxStudentsSize` attribute and assigns it to `_maxStudentsSize`. We also demonstrate its usage.

```javascript
import ClassRoom from "./0-classroom.js";

const room = new ClassRoom(10);
console.log(room._maxStudentsSize); // Output: 10
```

## 1. Let's make some classrooms

Here, we import the `ClassRoom` class and implement a function named `initializeRooms`. It returns an array of 3 `ClassRoom` objects with sizes 19, 20, and 34.

```javascript
import initializeRooms from './1-make_classrooms.js';

console.log(initializeRooms());
```

## 2. A Course, Getters, and Setters

We create a class called `HolbertonCourse` with constructor attributes `name`, `length`, and `students`. We add getters and setters for each attribute and ensure attribute type validation.

```javascript
import HolbertonCourse from "./2-hbtn_course.js";

const c1 = new HolbertonCourse("ES6", 1, ["Bob", "Jane"])
console.log(c1.name);
c1.name = "Python 101";
console.log(c1);
```

## 3. Methods, static methods, computed methods names..... MONEY

In this task, we implement a class called `Currency` with attributes `code` and `name`, and add getters and setters. We also add a method named `displayFullCurrency` to format the attributes.

```javascript
import Currency from "./3-currency.js";

const dollar = new Currency('$', 'Dollars');
console.log(dollar.displayFullCurrency()); // Output: Dollars ($)
```

## 4. Pricing

We create a class called `Pricing` with attributes `amount` and `currency` and add getters and setters. We also implement a method called `displayFullPrice` to format the attributes and a static method `convertPrice`.

```javascript
import Pricing from './4-pricing.js';
import Currency from './3-currency.js';

const p = new Pricing(100, new Currency("EUR", "Euro"))
console.log(p.displayFullPrice()); // Output: 100 Euro (EUR)
```

## 5. A Building

In this task, we implement an abstract class called `Building` with an attribute `sqft` and a getter. We require classes that extend `Building` to implement an `evacuationWarningMessage` method.

```javascript
import Building from './5-building.js';

const b = new Building(100);
console.log(b);

class TestBuilding extends Building {}

try {
    new TestBuilding(200)
}
catch(err) {
    console.log(err); // Output: Error: Class extending Building must override evacuationWarningMessage
}
```

## 6. Inheritance

We create a class called `SkyHighBuilding` that extends `Building`. It has attributes `sqft` and `floors`, and overrides the `evacuationWarningMessage` method.

```javascript
import SkyHighBuilding from './6-sky_high.js';

const building = new SkyHighBuilding(140, 60);
console.log(building.sqft);
console.log(building.floors);
console.log(building.evacuationWarningMessage()); // Output: Evacuate slowly the 60 floors
```

## 7. Airport

Here, we implement a class called `Airport` with attributes `name` and `code`. The default description returns the airport code.

```javascript
import Airport from "./7-airport.js";

const airportSF = new Airport('San Francisco Airport', 'SFO');
console.log(airportSF);
console.log(airportSF.toString());
```

## 8. Primitive - Holberton Class

In this task, we create a class called `HolbertonClass` with attributes `size` and `location`. When cast to a Number, it returns `size`, and when cast to a String, it returns `location`.

```javascript
import HolbertonClass from "./8-hbtn_class.js";

const hc = new HolbertonClass(12, "Mezzanine")
console.log(Number(hc)); // Output: 12
console.log(String(hc)); // Output: Mezzanine
```

## 9. Hoisting

We fix a code snippet involving the classes `HolbertonClass` and `StudentHolberton` and demonstrate the use of hoisting.

```javascript
import listOfStudents from "./9-hoisting.js";

console.log(listOfStudents);

const listPrinted = listOfStudents.map(
    student => student.fullStudentDescription
);

console.log(listPrinted);
```

## 10. Vroom

In the final task, we create a class called `Car` with attributes `brand`, `motor`, and `color`. We add a method called `cloneCar` that returns a new object of the class.

```javascript
import Car from "./10-car.js";

class TestCar extends Car {}

const tc1 = new TestCar("Nissan", "Turbo", "Pink");
const tc2 = tc1.cloneCar();

console.log(tc1);
console.log(tc1 instanceof TestCar);
console.log(tc2);
console.log(tc2 instanceof TestCar);
console.log(tc1 == tc2);
```

Feel free to use this README as a guide for your project. Good luck!
