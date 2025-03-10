----

.. _json-schema:

Component
=========
Test case with untyped list

Type: `object`

.. csv-table:: Component
   :header: "Property", "Type", "Required", "Description"

   :ref:`type <type>`, "`string`", "Optional", "Type"
   :ref:`ingress_cidr_blocks <ingress-cidr-blocks>`, "`array`", "Optional", "Ingress Cidr Blocks"

----

.. _type:

**type**

:Type: `string`
:Required: Optional
:Default: `"test"`
:Possible Values: `test`

----

.. _ingress-cidr-blocks:

**ingress_cidr_blocks**

A list of CIDR blocks allowed to connect.

:Type: `array`
:Required: Optional
:Possible Values: Any type
