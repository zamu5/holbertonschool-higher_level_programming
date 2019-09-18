#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int s, a, c = 0;
	PyObject *o;

	s = Py_SIZE(p);
	alloc = (*((PyListObject *)p)).allocated;
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", a);
	for (; c < s; c++)
	{
		printf("Element %d: ", c);
		o = PyList_GetItem(p, c);
		printf("%s\n", (*Py_TYPE(object)).tp_name);
	}
}
