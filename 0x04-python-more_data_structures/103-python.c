#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_bytes - print
 * @p: data
 */
void print_python_bytes(PyObject *p)
{
	size_t i, s = (*((PyVarObject *)p)).ob_size;
	char *str = (*((PyBytesObject *)p)).ob_sval;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %lu\n", s);
	printf("  trying string: %s\n", str);
	if (s >= 10)
		s = 10;
	else
		s++;
	printf("  first %lu bytes: ", s);
	for (i = 0; i < s; i++)
	{
		printf("%02x", str[i] & 0xff);
		if (i + 1 < s)
			printf(" ");
	}
	printf("\n");
}
/**
 * print_python_list - print
 * @p: data
 */
void print_python_list(PyObject *p)
{
	int i;
	PyObject *info;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", (*((PyVarObject *)p)).ob_size);
	printf("[*] Allocated = %lu\n", (*((PyListObject *)p)).allocated);
	for (i = 0; i < (*((PyVarObject *)p)).ob_size; i++)
	{
		info = (*((PyListObject *)p)).ob_item[i];
		printf("Element %d: %s\n", i, (*((*info).ob_type)).tp_name);
		if (PyBytes_Check(info))
			print_python_bytes(info);
	}
}
