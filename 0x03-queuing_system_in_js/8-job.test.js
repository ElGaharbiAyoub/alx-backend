import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should add jobs to the queue', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      // Add more jobs to the list as needed
    ];

    createPushNotificationsJobs(list, queue);

    expect(queue.testMode.jobs.length).toBe(list.length);

    list.forEach((job, index) => {
      expect(queue.testMode.jobs[index].type).toBe('push_notification_code_3');
      expect(queue.testMode.jobs[index].data).toEqual(job);
    });

    queue.testMode.jobs.forEach((job) => {
      job.on('complete', () => {
        expect(job.state()).toBe('complete');
      });
      job.on('failed', (err) => {
        expect(job.state()).toBe('failed');
        expect(err).toBe('Error: Job failed');
      });
      job.on('progress', (progress) => {
        expect(progress).toBe(100);
      });
    });
  });

  // Add more test cases as needed
});
