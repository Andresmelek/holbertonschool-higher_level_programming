#include "lists.h"
/**
 * insert_node - insterts a node
 * @head: pointer to the first node
 * @number: number
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new, *tmp = *head, *before;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if (tmp->n >= number)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}
	while (tmp)
	{
		if (tmp->n <= number)
		{
			before = tmp;
			tmp = tmp->next;
		}
		else
			break;
	}
	new->next = tmp;
	before->next = new;
	return (new);
}
