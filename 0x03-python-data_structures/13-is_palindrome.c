#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - function in C that checks if a singly linked list is a palindrome.
 * @head: double pointer to the first node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux;
	int i = 0, len = 0, j = 0;
	int buff[1000000];

	if (head == NULL || *head == NULL)
		return (1);

	aux = *head;
	while(aux)
	{
		buff[i] = aux->n;
		i++;
		aux = aux->next;
	}
	len = i - 1;
	while (j < len)
	{
		if (buff[len] != buff[j])
			return (0);
		len--;
		j++;
	}
	return (1);
}
