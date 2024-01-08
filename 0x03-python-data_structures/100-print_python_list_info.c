#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: a pointer to a Python list object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	/* check if p is a list object */
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid list object\n");
		return;
	}

	/* get the size and allocated memory of the list */
	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	/* print the size and allocated memory */
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	/* loop through the list elements and print their types */
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);							/* get the item at index i */
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
