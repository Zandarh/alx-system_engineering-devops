#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Runs an infinite while loop
 * Return: Zero
 */

int infinite_whille(void)
{
	while(1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * * main - Creates 5 zombie processess.
 * Return: Zero
 */

int main(void)
{
	pid_t pid;
	char zombies = 0;

	while (zombies < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			zombies++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
