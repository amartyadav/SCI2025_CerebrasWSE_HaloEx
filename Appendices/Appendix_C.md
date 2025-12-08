## Tasks In Depth

Again, the best explanation of tasks, task IDs, and types of tasks can be found in the SDK documentation.

### Important
The memcpy infrastructure uses colors 21, 22, 23, local task IDs 27, 28, 30, and control task IDs 33, 34, 35, 36, and 37. It also used microthread 0, input queue 0, and output queue 0. On WSE-3, memcpy additionally uses input queue 1. The compiler and runtime cannot detect all resource conflicts in your program. Do not use these resources in your program.

---

Find the relevant links here. These links will take you to the exact relevant sections of the SDK documentation.

- [Tasks in CSL](https://sdk.cerebras.net/csl/language/task-ids#task-identifiers-and-task-execution) - explains tasks, task IDs, types of tasks, and more.

You can skip the Control Tasks section if you are not using control tasks in your code (which we are not in this tutorial).
Pay attention to Local Taks, as they are used. And also refer to Data Tasks, as they are used very commonly.

