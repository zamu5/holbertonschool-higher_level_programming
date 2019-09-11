#include "lists.h"
/**
 * insert_node - insert a new sort node
 * @head: head of the list
 * @number: number to add
 * Return: the addres of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *c1, *c2, *new;

	if (!head || number <= 0)
		return (NULL);
	c1 = *head;
	if (c1 == NULL)
		add_nodeint_end(&c1, number);
	while (c1)
	{
		c2 = (*c1).next;
		if (c2 && number < (*c2).n)
		{
			new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);
			(*new).n = number;
			(*new).next = c2;
			(*c1).next = new;
			return (new);
		}
		c1 = (*c1).next;
	}
	return (NULL);
}
