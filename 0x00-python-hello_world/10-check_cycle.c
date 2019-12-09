#include "lists.h"
#include <stddef.h>
#include <stdarg.h>
#include <stdio.h>
/**
* check_cycle - finds the loop in the linked list
* @list: pointer to the first node
* Return: the address of the node where the loop starts
* or NULL if there is no loop
*/
int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);
	while (list)
	{
		if ((list->next) >= list)
		{
			return (1);
		}
		list = list->next;
	}
	return (0);
}
