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
	struct listint_s *temp = NULL;

	if (!head)
		return (NULL);
	c1 = *head;
	if (c1 == NULL)
	{
		temp = (struct listint_s *)malloc(sizeof(struct listint_s));
		if (temp == NULL)
			return (NULL);
		temp->n = number, temp->next = *head, *head = temp;
		return (temp);
	}
	while (c1)
	{
		c2 = (*c1).next;
		if (number < (*c1).n)
		{
			new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);
			(*new).n = number, (*new).next = c1, *head = new;
			return (new);

		}
		else if (c2 && number < (*c2).n)
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
	new = add_nodeint_end(head, number);
	return (NULL);
}
