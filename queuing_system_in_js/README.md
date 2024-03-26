# Queuing system in JS

This project implements a queuing system in JavaScript using Redis and various Node.js modules. It includes several tasks designed to create a robust queuing system with features such as job creation, processing, tracking progress, error handling, and data management.

## Tasks

### Task 0: Install a Redis instance

This task involves downloading, extracting, compiling the latest stable Redis version and setting up a Redis server. Additionally, it requires verifying the server's functionality and performing basic operations like setting and retrieving values.

### Task 1: Node Redis Client

In this task, a Redis client is created using the `node_redis` module. It involves connecting to the Redis server and handling connection errors. The script logs messages based on the connection status.

### Task 2: Node Redis client and basic operations

Building upon the previous task, this task adds functions to perform basic Redis operations like setting a new value and displaying the value of a key.

### Task 3: Node Redis client and async operations

This task introduces async operations using `promisify` to modify the function from Task 2 to use ES6 async/await syntax.

### Task 4: Node Redis client and advanced operations

In this task, more advanced Redis operations are performed, such as storing hash values using `hset` and retrieving them using `hgetall`.

### Task 5: Node Redis client publisher and subscriber

This task involves creating two scripts: one for a Redis subscriber and another for a publisher. The subscriber listens for messages on a channel and logs them, while the publisher sends messages to the channel after a certain time interval.

### Task 6: Create the Job creator

A job creator is implemented using Kue, a Redis-based job queue. It creates jobs with specified data and logs messages upon job creation, completion, and failure.

### Task 7: Create the Job processor

A job processor is developed using Kue to process jobs created by the job creator. It listens for new jobs, performs tasks based on job data, and logs messages accordingly.

### Task 8: Track progress and errors with Kue: Create the Job creator

This task extends the functionality of the job creator to track job progress and handle errors using Kue's features.

### Task 9: Track progress and errors with Kue: Create the Job processor

Similar to the previous task, this task enhances the job processor to track progress and handle errors effectively using Kue.

### Task 10: Writing the job creation function

A function named `createPushNotificationsJobs` is implemented to create multiple jobs using Kue. The function logs messages upon job creation, completion, and failure.

### Task 11: Writing the test for job creation

Tests are created for the `createPushNotificationsJobs` function to ensure it behaves as expected. The tests validate job creation, completion, and failure scenarios.

### Task 12: In stock?

This task involves creating an Express server to manage product data and stock using Redis. It includes routes to list products, view product details, and reserve products based on availability.

## Getting Started

To run the project, follow these steps:

1. Install Node.js and npm.
2. Install Redis and start the Redis server.
3. Clone the project repository.
4. Navigate to the project directory.
5. Install dependencies using `npm install`.
6. Run each task script using `npm run dev <script_name>`.

Make sure to follow the instructions provided in each task for setting up and running the scripts.

## Conclusion

This README provides an overview of the queuing system implemented in JavaScript using Redis and Node.js modules. Follow the tasks sequentially to understand and build upon each feature of the queuing system.