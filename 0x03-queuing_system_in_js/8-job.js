export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');
  jobs.forEach((job) => {
    const jobCreate = queue
      .create('push_notification_code_3', job)
      .save((err) => {
        if (!err) console.log(`Notification job created: ${jobCreate.id}`);
      });
    jobCreate.on('complete', () => {
      console.log(`Notification job ${jobCreate.id} completed`);
    });
    jobCreate.on('failed', (err) => {
      console.log(`Notification job ${jobCreate.id} failed: ${err}`);
    });
    jobCreate.on('progress', (progress) => {
      console.log(`Notification job ${jobCreate.id} ${progress}% complete`);
    });
  });
}
