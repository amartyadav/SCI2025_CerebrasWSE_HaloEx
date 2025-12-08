## Microthreads

The best explanation of microthreads, async DSD operations, and how they tie up, along with their restrictions can be found in the SDK documentation.

### Important
The memcpy infrastructure uses colors 21, 22, 23, local task IDs 27, 28, 30, and control task IDs 33, 34, 35, 36, and 37. It also used microthread 0, input queue 0, and output queue 0. On WSE-3, memcpy additionally uses input queue 1. The compiler and runtime cannot detect all resource conflicts in your program. Do not use these resources in your program.

---

Find the relevant links here. These links will take you to the exact relevant sections of the SDK documentation.

- [HW Resources and Async DSD Operations](https://sdk.cerebras.net/csl/language/dsds?highlight=input%20queue#hardware-resources-and-asynchronous-dsd-operations) - explains Microthreads, Async DSD operations, things to take care of when using them, and restrictions.
- [Microthread IDs](https://sdk.cerebras.net/csl/language/dsds?highlight=input%20queue#hardware-resources-and-asynchronous-dsd-operations) - explains Microthread IDs, usage and semantics, their properties, and how to block and unblock microthreads.