----

.. _json-schema:

JSON Schema
===========
JSON Schema missing a description, provide it using the `description` key in the root of the JSON document.

Type: `object`

.. csv-table:: 
   :header: "Property", "Type", "Required", "Description"

   :ref:`firstName <firstname>`, "`string`", "Optional", "The person's first name"
   :ref:`lastName <lastname>`, "`string`", "Optional", "The person's last name"
   :ref:`age <age>`, "`integer`", "Optional", "Age in years which must be equal :ref:`More <age>`"
   :ref:`email <email>`, "`string`", "Optional", "Email address of the person"

----

.. _firstname:

**firstName**

The person's first name.

:Type: `string`
:Required: Optional
:Possible Values: string

----

.. _lastname:

**lastName**

The person's last name.

:Type: `string`
:Required: Optional
:Possible Values: string

----

.. _age:

**age**

Age in years which must be equal to or greater than zero.

:Type: `integer`
:Required: Optional
:Default: `25`
:Possible Values: `0 <= x <= 150` and multiple of `1`

----

.. _email:

**email**

Email address of the person.

:Type: `string`
:Required: Optional
:Possible Values: Format: `email`
