#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks the prescence of cycles in a linked list
 * @list: list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	    listint_t *slow_p = list, *fast_p = list;

		while (slow_p && fast_p && fast_p->next)
		{
			slow_p = slow_p->next;
			fast_p = fast_p->next->next;
			if (slow_p == fast_p)
			{
				return (1);
			}
		}
		return (0);
}
