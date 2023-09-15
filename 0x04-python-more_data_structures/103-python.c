#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic information about a Python list object
 * @p: Pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object
 * @p: Pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	unsigned char *bytes;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes = (unsigned char *)PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %ld bytes: ", (size > 10) ? 10 : size);
	for (i = 0; i < ((size > 10) ? 10 : size); i++)
	{
		printf("%02x ", bytes[i]);
	}
	printf("\n");
}
