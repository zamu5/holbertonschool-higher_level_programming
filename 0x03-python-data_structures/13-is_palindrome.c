#include "lists.h"
/**
 * is_palindrome - check if the list is palindrome
 * @head: head of the list
 * Return: 0 if not or 1 if yes
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy;
	int cont = 0;

	if (head == NULL)
		return (1);
	copy = *head;
	while (copy != NULL)
		cont++, copy = (*copy).next;
	return(verify(head, cont));
}
int verify(listint_t **head, int cont)
{
	char vect[cont];
	listint_t *copy;
	int i = 0;

	copy = *head;
	while(copy != NULL)
	{
		vect[i] = (*copy).n;
		copy = (*copy).next;
		i++;
	}
	for(i = 0; i != cont; i++, cont--)
	{
		if (vect[i] != vect[cont - 1])
			return (0);
	}
	return (1);

}
