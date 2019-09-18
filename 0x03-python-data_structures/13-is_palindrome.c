#include "lists.h"
/**
 * is_palindrome - check if the list is palindrome
 * @head: head of the list
 * Return: 0 if not or 1 if yes
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy, *st, *ts;
	int cont = 0, i = 0, pal, j = 0;

	if (head == NULL)
		return (1);
	copy = *head;
	while (copy != NULL)
		cont++, copy = (*copy).next;
	st = *head;
	pal = cont - 1;
	while (i < cont / 2)
	{
		ts = st;
		while (j != pal)
		{
			ts = (*ts).next;
			j++;
		}
		if ((*ts).n != (*st).n)
			return (0);
		st = (*st).next;
		pal = pal - 2;
		j = 0;
		i++;
	}
	return (1);
}
