----

.. _def-json-schema:

JSON Schema
===========
JSON Schema missing a description, provide it using the `description` key in the root of the JSON document.

Type: `object`

.. csv-table::
   :header: "Property", "Type", "Required", "Description"

   ":ref:`Foobar <prop-foobar>`", "`object`", "Required", ""
   ":ref:`Foobaz <prop-foobaz>`", "`array`", "Required", ""

----

.. _prop-foobar:

**Foobar**

:Type: `object`
:Required: Required
:Possible Values: object

.. csv-table::
   :header: "Property", "Type", "Required", "Description"

   ":ref:`A <prop-foobar-a>`", "`string`", "Optional", ""
   ":ref:`B <prop-foobar-b>`", "`string`", "Optional", ""

----

.. _prop-foobar-a:

:ref:`Foobar <prop-foobar>` > **A**

:Type: `string`
:Required: Optional
:Possible Values: string

----

.. _prop-foobar-b:

:ref:`Foobar <prop-foobar>` > **B**

:Type: `string`
:Required: Optional
:Possible Values: string

----

.. _prop-foobaz:

**Foobaz**

:Type: `array`
:Required: Required
:Possible Values: object
