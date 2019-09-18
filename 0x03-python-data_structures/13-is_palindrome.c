#include "lists.h"
/**
 * is_palindrome - check if the list is palindrome
 * @head: head of the list
 * Return: 0 if not or 1 if yes
 */
int is_palindrome(listint_t **head)
{
	int vect[999999];
	listint_t *copy;
	int i = 0, cont = 0;

	if (*head == NULL)
		return (1);
	if (head == NULL)
		return (0);
	copy = *head;
	while(copy != NULL)
	{
		vect[cont] = (*copy).n;
		copy = (*copy).next;
		cont++;
	}
	for(i = 0; i != cont; i++, cont--)
	{
		if (vect[i] != vect[cont - 1])
			return (0);
	}
	return (1);

}
