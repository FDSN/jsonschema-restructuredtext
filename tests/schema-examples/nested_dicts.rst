----

.. _json-schema:

JSON Schema
===========
JSON Schema missing a description, provide it using the `description` key in the root of the JSON document.

Type: `object`

.. csv-table:: 
   :header: "Property", "Type", "Required", "Description"

   :ref:`Foobar <foobar>`, "`object`", "Required", ""
   :ref:`Foobaz <foobaz>`, "`array`", "Required", ""

----

.. _foobar:

**Foobar**

:Type: `object`
:Required: Required
:Possible Values: object

.. csv-table:: 
   :header: "Property", "Type", "Required", "Description"

   :ref:`A <foobar-a>`, "`string`", "Optional", ""
   :ref:`B <foobar-b>`, "`string`", "Optional", ""

----

.. _foobar-a:

   :ref:`Foobar <foobar>` > **A**

   :Type: `string`
   :Required: Optional
   :Possible Values: string

----

.. _foobar-b:

   :ref:`Foobar <foobar>` > **B**

   :Type: `string`
   :Required: Optional
   :Possible Values: string

----

.. _foobaz:

**Foobaz**

:Type: `array`
:Required: Required
:Possible Values: object
