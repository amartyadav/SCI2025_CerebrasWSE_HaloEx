## Other Important Langauge Features
There are other important language features that are used in the tutorial code, but were not explained in the main tutorial as they were provided in the code already due to their complexity, lack of time, or being out of scope for the main tutorial.

Like any other language and architecture, WSE-3 and CSL have many features that are useful to know about, and that can be used to optimize code, or enable certain functionality.

I am linking to the relevant sections for the important concets of the SDK documentation that explain these features in depth, so you can read up on them as needed. 

- [Builtins](https://sdk.cerebras.net/csl/language/builtins_) - These are the calls that you saw in the code, like `@get_dsd`, etc. Builtins are like library functions that are built into CSL and WSE-3, and provide optimised access to hardware, or other common programming calls.
Usually better to use them instead of writing your own code for the same functionality, as they are optimised for the hardware.

- [Comptime](https://sdk.cerebras.net/csl/language/comptime) - In CSL, it is possible to ensure that code is executed at compile-time by using the comptime keyword, which guarantees that the code will have no run-time footprint. An error is emitted if compile-time evaluation is not possible. This is useful in a lot of scenarios, with some language features like DSDs using comptime extensively for their indices in tensor-access expressions. Useful to know.

- [Libraries](https://sdk.cerebras.net/csl/language/libraries) - CSL has a set of built-in libraries that provide useful functionality, like math functions, code timing, malloc, dsd_ops, etc. These libraries can be imported and used in your code. Knowing about these libraries can help you write more efficient and effective code.

- [Libraries for WSE-3](https://sdk.cerebras.net/csl/language/libraries_wse3) - These are libraries that are specific to WSE-3, and provide functionality that is unique to the WSE-3 architecture. Knowing about these libraries can help you take advantage of the unique features of WSE-3. In particular, the `<message_passing>` library is useful to know about, as it provides functions for sending and receiving messages between PEs. This is not entirely optimised for complex tasks yet, so don't expect MPI like functionality, but it is a good start. Work is ongoing to improve this in the next SDK versions.

- [CSL Syntax Overview](https://sdk.cerebras.net/csl/language/syntax) - A good overview of the CSL syntax, useful to refer to when writing code.

- [Debugging Guide](https://sdk.cerebras.net/debug/debugging) - Extreely useful guide on how to debug CSL code, and the various tools available for debugging. Highly recommended to read through this guide to understand how to effectively debug CSL code.