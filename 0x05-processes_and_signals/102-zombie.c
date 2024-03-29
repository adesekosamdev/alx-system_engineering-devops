#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - infinite loop
 * Return: no return
**/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: no return
**/

int main(void)
{
	pid_t zombie;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie > 0)
		{
			printf("Zombie process created, PID: %d\n", zombie);
			sleep(1);
		}
		else
			exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
