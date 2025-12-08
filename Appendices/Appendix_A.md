## Input Queues and Output Queues

### Definitions
#### Input Queues
An input queue is a hardware buffer where data is temporarily stored before entering the compute engine (CE) of a PE.
#### Output Queues
An output queue is a hardware buffer where data is temporarily stored after being processed by the CE before being sent to its destination.

---

### Important
The memcpy infrastructure uses colors 21, 22, 23, local task IDs 27, 28, 30, and control task IDs 33, 34, 35, 36, and 37. It also used microthread 0, input queue 0, and output queue 0. On WSE-3, memcpy additionally uses input queue 1. The compiler and runtime cannot detect all resource conflicts in your program. Do not use these resources in your program.

---

To understand this better, an understanding of `tasks, task IDs and type of tasks` is required.

#### Task IDs and Types of Tasks
The term “task identifier” or “task ID” is used to refer to a numerical value that can be associated with a task. A task ID is a number from 0 to 63. Within this range there are two properties that further distinguish a task ID: routable and activatable.

There exist three types of tasks, each with an associated task ID handle type:

- The first are data tasks. These are associated with a data_task_id, which on the WSE-2 architecture is created from a routable identifier associated with a color. On the WSE-3 architecture, a data_task_id is created from an input queue, which also must be associated with a color. An input queue is a hardware buffer where data is temporarily stored before entering the compute engine (CE) of a PE.

- The second are local tasks. These are associated with a local_task_id, which is created from an activatable identifier.

- The third are control tasks. These are associated with a control_task_id, which can be created from any identifier, including those that are neither routable nor activatable.

Both data tasks and control tasks are a type of wavelet-triggered task, or WTT: their activation is triggered by the arrival of a wavelet.

_On WSE-2, task IDs 0 to 23 are the routable task IDs, as data tasks IDs are created from one of the 24 routable colors. On WSE-3, task IDs 0 to 7 are the routable task IDs, as data task IDs are created from one of the 8 input queues._

On WSE-2, the task ID is the same as the color ID: it takes on a value between 0 and 23. On WSE-3, this task ID is instead the ID of an input queue which is bound to the color: it takes on a value between 0 and 7.

This setup can be seen in depth in the pe.csl file in the code provided. See how each color is bound to a queue, and how each queue is assigned a task ID. This can be seen at the very bottom of the pe.csl file, and in the `comptime` block at the end of the file.

