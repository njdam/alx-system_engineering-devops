# Processes and signals

I. [A process]() is a running instance of a program or a task on a computer. It represents the execution of a specific program and has its own memory space and resources. Processes are managed by the operating system, and each process is identified by a unique PID.

[A PID (Process ID)]() is a unique numerical identifier assigned to a running process in a Unix-like operating system. It is used by the system to track and manage processes. Each process in the system has a unique PID.

[How to Kill a Process:]()
To kill (terminate) a process, you can use the kill command, followed by the PID of the process you want to terminate. By default, the kill command sends the SIGTERM signal to the process, asking it to terminate gracefully. If needed, you can use the SIGKILL signal with the -9 option to forcefully terminate a process.

II. [A signal]() is a software interrupt delivered to a process by the operating system. Signals are used to communicate with processes and can be used for various purposes, such as terminating a process, stopping a process, or asking a process to reload its configuration.

[Two Signals That Cannot Be Ignored:]()
The two signals that cannot be ignored by a process are:

`SIGKILL` ([signal number 9]()): This signal forces a process to terminate immediately and cannot be caught or ignored. It is often used to forcibly terminate unresponsive processes.

`SIGSTOP` ([signal number 19 or 17]()): This signal stops a process temporarily, and it cannot be caught or ignored. It effectively puts the process in a suspended state.

[Note That:]() Other commonly used signals include SIGTERM (15) to ask a process to terminate gracefully and SIGHUP (1) to instruct a process to reload its configuration.


[MANUAL PAGE]()

1. [`ps`:]()

The `ps` command is used to display information about running processes on a Unix-like operating system. It provides details such as the PID, terminal, CPU and memory usage, process state, and more.


2. [`pgrep` and `pkill`:]()

=> `pgrep`: The pgrep command is used to find the PIDs of processes based on their names or other attributes.

=> `pkill`: The `pkill` command is used to send signals to processes based on their names or other attributes. It is often used to terminate processes based on their names.


3. [`exit`:]()

The `exit` command is used to terminate a script or a shell session. When used in a script, it exits the script with a specific exit code. In an interactive shell, it terminates the shell session.


4. [`trap`:]()

The trap command is used to set up actions to be taken when a signal is received by a process. It allows you to handle signals in a custom way and take appropriate actions when specific signals are received.

## SIGNAL NUMBERS

Unix-like operating systems, there are various signal numbers that can be used to communicate with processes and control their behavior.

Here are some commonly used signal numbers along with their corresponding names:

1. [`SIGHUP` (1): Hangup signal]()
This signal is typically sent to a process when its controlling terminal is closed.

2. [`SIGINT` (2): Interrupt signal]()
This signal is sent to a process when the user presses Ctrl+C on the terminal. It is used to request the process to terminate gracefully.

3. [`SIGQUIT` (3): Quit signal]()
This signal is similar to SIGINT but is typically used to request the process to generate a core dump for debugging purposes.

4. [`SIGKILL` (9): Kill signal]()
This signal cannot be caught or ignored by the process and immediately terminates it.

5. [`SIGTERM` (15): Termination signal]()
This signal is typically sent to request the process to terminate gracefully. It allows the process to perform cleanup operations before exiting.

6. [`SIGSTOP` (19): Stop signal]()
This signal is used to suspend the execution of a process. It cannot be caught or ignored.

7. [`SIGCONT` (18): Continue signal]()
This signal is used to resume the execution of a previously stopped process.

8. [`SIGUSR1` (10) and `SIGUSR2` (12): User-defined signals]()
These signals can be used by user applications to communicate custom actions to processes.

9. [`SIGPIPE` (13): Broken pipe signal]()
This signal is sent to a process when it attempts to write to a pipe that has been closed.

10. [`SIGALRM` (14): Alarm signal]()
This signal is sent to a process when the timer set by the alarm function expires.

[Note That:]() These are just a few examples of commonly used signals. There are many other signals defined in Unix systems, each with its specific purpose. Different signals are used for different scenarios and tasks, such as process control, communication, error handling, and more. Each signal serves a specific role in managing and interacting with processes in the system.
