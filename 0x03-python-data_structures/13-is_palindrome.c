#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
int num_nodes(listint_t *head);
void free_array(int *array, int len);
/**
 * num_nodes - return num of nodes in a linked list
 * @head: head node
 * Return: num of nodes
*/
int num_nodes(listint_t *head)
{
	int t = 1;
	listint_t *current;

	if (!head)
	{
		return (0);
	}
	current = head;
	while (current && current->next)
	{
		current = current->next;
		t++;
	}
	return (t);
}
/**
 * free_array - frees an int malloced array
 * @array: int array
 * @len: length of array
void free_array(int *array, int len)
{
	int i;

	for (i = 0; i < len; i++)
	{
		free(array[i]);
	}
	free(array);
}*/
/**
 * is_palindrome - checks palindrome list
 * @head: pointer to head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	int l = 0, k, i = 0, len, *array;
	listint_t *current;

	len = num_nodes(*head);
	array = malloc(sizeof(int) * len);
	current = *head;
	while (i < len)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}
	k = len - 1;
	while (k > l)
	{
		if (array[l] != array[k])
		{
			free(array);
			return (0);
		}
		l++;
		k--;
	}
	free(array);
	return (1);
}
