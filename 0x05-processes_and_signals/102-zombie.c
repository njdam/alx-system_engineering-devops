#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - a function to sleep 1 second;
 * After creation parent process and zombie;
 *
 * Return: value 0 always.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - is a function to create parent process and zombie;
 *
 * Return: value 0 always.
 */
int main(void)
{
	pid_t ZOMBIE_PID;
	int i = 0;

	while (i < 5)
	{
		ZOMBIE_PID = fork();
		if (ZOMBIE_PID == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", ZOMBIE_PID);
		i++;
	}

	infinite_while();

	return (0);
}
