#include "lists.h"
int check_cycle(listint_t *list)
{
listint_t *copy1, *copy2;

	copy1 = list;
	if (list == NULL)
		return (0);
	if (list == (*list).next)
		return (1);
	while (copy1 != NULL && (*copy1).next)
	{
		copy1 = (*copy1).next;
		copy2 = list;
		while (copy1 && copy2 != copy1)
		{
			if (copy2 == NULL)
				return (0);
 			if (copy2 == (*copy1).next)
				return (1);
			copy2 = (*copy2).next;
		}
	}
	return (0);
}
