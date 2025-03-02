----

.. _jsonschema-restructuredtext:

Person
======
JSON Schema missing a description, provide it using the `description` key in the root of the JSON document.

Type: `object`

.. csv-table:: Person
   :header: "Property", "Type", "Required", "Description"

   :ref:`firstName <firstname>`, "`string`", "Optional", "The person's first name"
   :ref:`lastName <lastname>`, "`string`", "Optional", "The person's last name"
   :ref:`age <age>`, "`integer`", "Optional", "Age in years which must be equal :ref:`More <age>`"

----

.. _firstname:

.. rubric:: firstName

The person's first name.

:Type: `string`

:Required: Optional

:Possible Values: string


----

.. _lastname:

.. rubric:: lastName

The person's last name.

:Type: `string`

:Required: Optional

:Possible Values: string


----

.. _age:

.. rubric:: age

Age in years which must be equal to or greater than zero.

:Type: `integer`

:Required: Optional

:Possible Values: `0 <= x`
