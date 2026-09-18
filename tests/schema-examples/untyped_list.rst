----

.. _def-json-schema:

Component
=========
Test case with untyped list

Type: `object`

.. csv-table:: Component
   :header: "Property", "Type", "Required", "Description"

   ":ref:`type <prop-type>`", "`string`", "Optional", "Type"
   ":ref:`ingress_cidr_blocks <prop-ingress-cidr-blocks>`", "`array`", "Optional", "Ingress Cidr Blocks"

----

.. _prop-type:

**type**

:Type: `string`
:Required: Optional
:Default: ``"test"``
:Possible Values: ``"test"``

----

.. _prop-ingress-cidr-blocks:

**ingress_cidr_blocks**

A list of CIDR blocks allowed to connect.

:Type: `array`
:Required: Optional
:Default: ``[]``
:Possible Values: Any type
