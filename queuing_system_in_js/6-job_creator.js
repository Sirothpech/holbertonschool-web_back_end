import { createQueue } from 'kue';

const queue = createQueue();

const data = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
}

const job = queue.create('push_notification_code', data)
.on('complete', function() {
    console.log('Notification job completed');
})
.on('failed', function() {
    console.log('Notification job failed');
});

job.save((error) => {
    console.log(`Notification job created: ${job.id}`);
});
