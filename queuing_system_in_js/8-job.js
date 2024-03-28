export default function createPushNotificationJobs(jobs, queue) {
    if(!(jobs instanceof Array)) {
        throw Error('Jobs is not an array')
    };
    for (const item of jobs) {
        const job = queue.create('push_notification_code_3', item)
        .on('complete', function() {
            console.log(`Notification job ${job.id} completed`);
        })
        .on('failed', function(error) {
            console.log(`Notification job ${job.id} failed: ${error}`);
        })
        .on('progress', function(progress) {
        console.log(`Notification job ${job.id} ${progress}% complete`);
        });
    
        job.save((error) => {
            if (!error) console.log(`Notification job created: ${job.id}`);
        });
    };
}