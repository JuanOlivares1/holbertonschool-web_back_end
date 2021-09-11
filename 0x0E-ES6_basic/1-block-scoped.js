export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = function task() {
      const task = true;
      return task;
    };
    const task2 = function task2() {
      const task2 = false;
      return task2;
    };
    task();
    task2();
  }

  return [task, task2];
}
