#include <python3.10/Python.h>

int main()
{
	Py_Initialize();

	PyObject *myString = Py_BuildValue("s", "Hello from C!");

	if (myString != NULL)
	{
		PyObject_Print(myString, stdout, 0);
		printf("\n");

		Py_DECREF(myString);
	}
	else
	{
		PyErr_Print();
	}

	Py_Finalize();

	return (0);
}
