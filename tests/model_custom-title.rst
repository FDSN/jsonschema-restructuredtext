----

.. _def-car-(custom-title):

Car
===
This is the description of the Car.

New lines work.
UTF-8 characters work: áéíóú
👍

Type: `object`

.. csv-table:: Car
   :header: "Property", "Type", "Required", "Description"

   ":ref:`brand <prop-brand>`", "`string`", "Required", "Brand"
   ":ref:`model <prop-model>`", "`string`", "Required", "Model"
   ":ref:`year <prop-year>`", "`integer`", "Required", "Year"
   ":ref:`car_class <prop-car-class>`", "`object`", "Required", "The class of the car"
   ":ref:`engine <prop-engine>`", "`object`", "Required", "The engine of the car"
   ":ref:`color <prop-color>`", "`string`", "Required", "Color"
   ":ref:`kms <prop-kms>`", "`integer`", "Optional", "Kms"
   ":ref:`manufacturer_config <prop-manufacturer-config>`", "`array`", "Optional", "Manufacturer Config"
   ":ref:`extra_pack <prop-extra-pack>`", "`object` or `null`", "Optional", "Extra Pack"
   ":ref:`brand_country <prop-brand-country>`", "`string`", "Required", "Brand Country"

----

.. _prop-brand:

**brand**

The brand of the car.

:Type: `string`
:Required: Required
:Possible Values: Length: `1 <= string <= 100`
:Examples: ``"Ford"``, ``"Toyota"``

----

.. _prop-model:

**model**

The model of the car.

:Type: `string`
:Required: Required
:Possible Values: Length: `1 <= string <= 100`
:Examples: ``"Focus"``, ``"Corolla"``

----

.. _prop-year:

**year**

The year of the car.

:Type: `integer`
:Required: Required
:Possible Values: `1900 < x < 2100`

----

.. _prop-car-class:

**car_class**

The class of the car.

:Type: `object`
:Required: Required
:Possible Values: :ref:`CarClass <def-carclass>`
:Examples: ``{"doors": 5, "passengers": 5, "type": "sedan"}``, ``{"doors": 3, "passengers": 2, "type": "hatchback"}``, ``{"doors": 5, "passengers": 5, "type": "suv"}``

----

.. _prop-engine:

**engine**

The engine of the car.

:Type: `object`
:Required: Required
:Possible Values: :ref:`Engine <def-engine>`

----

.. _prop-color:

**color**

The color of the car.

:Type: `string`
:Required: Required
:Possible Values: Length: `1 <= string <= 100`

----

.. _prop-kms:

**kms**

The number of kilometers the car has.

:Type: `integer`
:Required: Optional
:Possible Values: integer

----

.. _prop-manufacturer-config:

**manufacturer_config**

The manufacturer's extras.

:Type: `array`
:Required: Optional
:Default: `[]`
:Possible Values: :ref:`Airbag <def-airbag>` and/or :ref:`NavigationSystem <def-navigationsystem>` and/or :ref:`Upholstery <def-upholstery>`

----

.. _prop-extra-pack:

**extra_pack**

The extra pack of the car.

:Type: `object` or `null`
:Required: Optional
:Possible Values: :ref:`ExtraPackAdvanced <def-extrapackadvanced>` and/or :ref:`ExtraPackBasic <def-extrapackbasic>`

----

.. _prop-brand-country:

**brand_country**

[Deprecated] The country where the brand is from.

:Type: `string`
:Required: Required
:Possible Values: `^[A-Z]{2}$ <https://regex101.com/?regex=%5E%5BA-Z%5D%7B2%7D%24>`_

----

.. _def-airbag:

Airbag
------
This is the description of the Airbag.

Type: `object`

.. csv-table:: Airbag
   :header: "Property", "Type", "Required", "Description"

   ":ref:`type <prop-airbag-type>`", "`string`", "Required", "Type"

----

.. _prop-airbag-type:

:ref:`Airbag <def-airbag>` > **type**

The type of airbag.

:Type: `string`
:Required: Required
:Possible Values: `front` `side` `curtain`

----

.. _def-carclass:

Class
-----
This is the description of the CarClass.

Type: `object`

.. csv-table:: Class
   :header: "Property", "Type", "Required", "Description"

   ":ref:`type <prop-carclass-type>`", "`string`", "Required", "Type"
   ":ref:`doors <prop-carclass-doors>`", "`integer`", "Optional", "Doors"
   ":ref:`passengers <prop-carclass-passengers>`", "`integer`", "Optional", "Passengers"

----

.. _prop-carclass-type:

:ref:`CarClass <def-carclass>` > **type**

The type of car.

:Type: `string`
:Required: Required
:Possible Values: `sedan` `hatchback` `suv`

----

.. _prop-carclass-doors:

:ref:`CarClass <def-carclass>` > **doors**

The number of doors the car has.

:Type: `integer`
:Required: Optional
:Default: `5`
:Possible Values: integer

----

.. _prop-carclass-passengers:

:ref:`CarClass <def-carclass>` > **passengers**

The number of passengers the car can carry.

:Type: `integer`
:Required: Optional
:Default: `5`
:Possible Values: integer

----

.. _def-engine:

Engine
------
This is the description of the Engine.

**Markdown works**. *Italic*. **Bold**. ***Bold and italic***.
- [] Unchecked
- [x] Checked

Type: `object`

.. csv-table:: Engine
   :header: "Property", "Type", "Required", "Description"

   ":ref:`model <prop-engine-model>`", "`string`", "Required", "Model"
   ":ref:`power <prop-engine-power>`", "`integer`", "Required", "Power"
   ":ref:`fuel_type <prop-engine-fuel-type>`", "`string`", "Required", "Fuel Type"
   ":ref:`liters <prop-engine-liters>`", "`number`", "Required", "Liters"
   ":ref:`turbo <prop-engine-turbo>`", "`boolean`", "Optional", "Turbo"

----

.. _prop-engine-model:

:ref:`Engine <def-engine>` > **model**

The name of the engine model.

:Type: `string`
:Required: Required
:Possible Values: Length: `1 <= string <= 100`

----

.. _prop-engine-power:

:ref:`Engine <def-engine>` > **power**

The power of the engine in HP.

:Type: `integer`
:Required: Required
:Possible Values: integer

----

.. _prop-engine-fuel-type:

:ref:`Engine <def-engine>` > **fuel_type**

The type of fuel the engine uses.

:Type: `string`
:Required: Required
:Possible Values: `gasoline` `diesel` `electric`

----

.. _prop-engine-liters:

:ref:`Engine <def-engine>` > **liters**

The displacement of the engine in liters.

:Type: `number`
:Required: Required
:Possible Values: `0 < x`

----

.. _prop-engine-turbo:

:ref:`Engine <def-engine>` > **turbo**

Whether the engine has a turbo or not.

:Type: `boolean`
:Required: Optional
:Default: `false`
:Possible Values: boolean

----

.. _def-extrapackadvanced:

ExtraPackAdvanced
-----------------
This is the description of the ExtraPack2.

Type: `object`

.. csv-table:: ExtraPackAdvanced
   :header: "Property", "Type", "Required", "Description"

   ":ref:`heated_seats <prop-extrapackadvanced-heated-seats>`", "`boolean`", "Optional", "Heated Seats"
   ":ref:`heated_steering_wheel <prop-extrapackadvanced-heated-steering-wheel>`", "`boolean`", "Optional", "Heated Steering Wheel"
   ":ref:`parking_sensors <prop-extrapackadvanced-parking-sensors>`", "`boolean`", "Optional", "Parking Sensors"
   ":ref:`adaptive_cruise_control <prop-extrapackadvanced-adaptive-cruise-control>`", "`boolean`", "Optional", "Adaptive Cruise Control"

----

.. _prop-extrapackadvanced-heated-seats:

:ref:`ExtraPackAdvanced <def-extrapackadvanced>` > **heated_seats**

Whether the car has heated seats.

:Type: `boolean`
:Required: Optional
:Default: `true`
:Possible Values: boolean

----

.. _prop-extrapackadvanced-heated-steering-wheel:

:ref:`ExtraPackAdvanced <def-extrapackadvanced>` > **heated_steering_wheel**

Whether the car has a heated steering wheel.

:Type: `boolean`
:Required: Optional
:Default: `true`
:Possible Values: boolean

----

.. _prop-extrapackadvanced-parking-sensors:

:ref:`ExtraPackAdvanced <def-extrapackadvanced>` > **parking_sensors**

Whether the car has parking sensors.

:Type: `boolean`
:Required: Optional
:Default: `true`
:Possible Values: boolean

----

.. _prop-extrapackadvanced-adaptive-cruise-control:

:ref:`ExtraPackAdvanced <def-extrapackadvanced>` > **adaptive_cruise_control**

Whether the car has adaptive cruise control

:Type: `boolean`
:Required: Optional
:Default: `true`
:Possible Values: boolean

----

.. _def-extrapackbasic:

ExtraPackBasic
--------------
This is the description of the ExtraPack1.

Type: `object`

.. csv-table:: ExtraPackBasic
   :header: "Property", "Type", "Required", "Description"

   ":ref:`heated_seats <prop-extrapackbasic-heated-seats>`", "`boolean`", "Optional", "Heated Seats"
   ":ref:`heated_steering_wheel <prop-extrapackbasic-heated-steering-wheel>`", "`boolean`", "Optional", "Heated Steering Wheel"
   ":ref:`parking_sensors <prop-extrapackbasic-parking-sensors>`", "`boolean`", "Optional", "Parking Sensors"

----

.. _prop-extrapackbasic-heated-seats:

:ref:`ExtraPackBasic <def-extrapackbasic>` > **heated_seats**

Whether the car has heated seats.

:Type: `boolean`
:Required: Optional
:Default: `false`
:Possible Values: boolean

----

.. _prop-extrapackbasic-heated-steering-wheel:

:ref:`ExtraPackBasic <def-extrapackbasic>` > **heated_steering_wheel**

Whether the car has a heated steering wheel.

:Type: `boolean`
:Required: Optional
:Default: `false`
:Possible Values: boolean

----

.. _prop-extrapackbasic-parking-sensors:

:ref:`ExtraPackBasic <def-extrapackbasic>` > **parking_sensors**

Whether the car has parking sensors.

:Type: `boolean`
:Required: Optional
:Default: `true`
:Possible Values: boolean

----

.. _def-navigationsystem:

NavigationSystem
----------------
This is the description of the NavigationSystem.

Type: `object`

.. csv-table:: NavigationSystem
   :header: "Property", "Type", "Required", "Description"

   ":ref:`type <prop-navigationsystem-type>`", "`string`", "Required", "Type"

----

.. _prop-navigationsystem-type:

:ref:`NavigationSystem <def-navigationsystem>` > **type**

The type of navigation system.

:Type: `string`
:Required: Required
:Possible Values: `gps` `carplay` `androidauto`

----

.. _def-upholstery:

Upholstery
----------
This is the description of the Upholstery.

Type: `object`

.. csv-table:: Upholstery
   :header: "Property", "Type", "Required", "Description"

   ":ref:`type <prop-upholstery-type>`", "`string`", "Required", "Type"
   ":ref:`stitching <prop-upholstery-stitching>`", "`object`", "Optional", "Stitching"

----

.. _prop-upholstery-type:

:ref:`Upholstery <def-upholstery>` > **type**

The type of upholstery.

:Type: `string`
:Required: Required
:Possible Values: `leather` `fabric`

----

.. _prop-upholstery-stitching:

:ref:`Upholstery <def-upholstery>` > **stitching**

Metadata about the stitching.

:Type: `object`
:Required: Optional
:Default: `{}`
:Possible Values: object
