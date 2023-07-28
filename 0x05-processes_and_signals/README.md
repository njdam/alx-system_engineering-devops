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

