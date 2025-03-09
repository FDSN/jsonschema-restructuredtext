----

.. _car-(custom-title):

Car
===
This is the description of the Car.

New lines work.
UTF-8 characters work: áéíóú
👍

Type: `object`

.. csv-table:: Car
   :header: "Property", "Type", "Required", "Description"

   :ref:`brand <brand>`, "`string`", "Required", "Brand"
   :ref:`brand_country <brand-country>`, "`string`", "Required", "Brand Country"
   :ref:`model <model>`, "`string`", "Required", "Model"
   :ref:`year <year>`, "`integer`", "Required", "Year"
   :ref:`car_class <car-class>`, "`object`", "Required", "The class of the car"
   :ref:`engine <engine>`, "`object`", "Required", "The engine of the car"
   :ref:`kms <kms>`, "`integer`", "Required", "Kms"
   :ref:`color <color>`, "`string`", "Required", "Color"
   :ref:`manufacturer_config <manufacturer-config>`, "`array`", "Required", "Manufacturer Config"
   :ref:`extra_pack <extra-pack>`, "`object` or `null`", "Required", "Extra Pack"

----

.. _brand:

**brand**

The brand of the car.

:Type: `string`
:Required: Required
:Possible Values: Length: `1 <= string <= 100`
:Examples: ``Ford``, ``Toyota``

----

.. _brand-country:

**brand_country**

[Deprecated] The country where the brand is from.

:Type: `string`
:Required: Required
:Possible Values: `^[A-Z]{2}$ <https://regex101.com/?regex=%5E%5BA-Z%5D%7B2%7D%24>`_

----

.. _model:

**model**

The model of the car.

:Type: `string`
:Required: Required
:Possible Values: Length: `1 <= string <= 100`
:Examples: ``Focus``, ``Corolla``

----

.. _year:

**year**

The year of the car.

:Type: `integer`
:Required: Required
:Possible Values: `1900 < x < 2100`

----

.. _car-class:

**car_class**

The class of the car.

:Type: `object`
:Required: Required
:Possible Values: [CarClass](#carclass)
:Examples: ``{'doors': 5, 'passengers': 5, 'type': 'sedan'}``, ``{'doors': 3, 'passengers': 2, 'type': 'hatchback'}``, ``{'doors': 5, 'passengers': 5, 'type': 'suv'}``

----

.. _engine:

**engine**

The engine of the car.

:Type: `object`
:Required: Required
:Possible Values: [Engine](#engine)

----

.. _kms:

**kms**

The number of kilometers the car has.

:Type: `integer`
:Required: Required
:Possible Values: integer

----

.. _color:

**color**

The color of the car.

:Type: `string`
:Required: Required
:Possible Values: Length: `1 <= string <= 100`

----

.. _manufacturer-config:

**manufacturer_config**

The manufacturer's extras.

:Type: `array`
:Required: Required
:Possible Values: [Airbag](#airbag) and/or [NavigationSystem](#navigationsystem) and/or [Upholstery](#upholstery)


----

.. _extra-pack:

**extra_pack**

The extra pack of the car.

:Type: `object` or `null`
:Required: Required
:Possible Values: [ExtraPackAdvanced](#extrapackadvanced) and/or [ExtraPackBasic](#extrapackbasic)

----

.. _airbag:

Airbag
------
This is the description of the Airbag.

Type: `object`

.. csv-table:: Airbag
   :header: "Property", "Type", "Required", "Description"

   :ref:`type <airbag-type>`, "`string`", "Required", "Type"

----

.. _airbag-type:

:ref:`Airbag <airbag>` > **type**

The type of airbag.

:Type: `string`
:Required: Required
:Possible Values: `front` `side` `curtain`

----

.. _carclass:

Class
-----
This is the description of the CarClass.

Type: `object`

.. csv-table:: Class
   :header: "Property", "Type", "Required", "Description"

   :ref:`type <carclass-type>`, "`string`", "Required", "Type"
   :ref:`doors <carclass-doors>`, "`integer`", "Required", "Doors"
   :ref:`passengers <carclass-passengers>`, "`integer`", "Required", "Passengers"

----

.. _carclass-type:

:ref:`CarClass <carclass>` > **type**

The type of car.

:Type: `string`
:Required: Required
:Possible Values: `sedan` `hatchback` `suv`

----

.. _carclass-doors:

:ref:`CarClass <carclass>` > **doors**

The number of doors the car has.

:Type: `integer`
:Required: Required
:Default: `5`
:Possible Values: integer

----

.. _carclass-passengers:

:ref:`CarClass <carclass>` > **passengers**

The number of passengers the car can carry.

:Type: `integer`
:Required: Required
:Default: `5`
:Possible Values: integer

----

.. _engine:

Engine
------
This is the description of the Engine.

**Markdown works**. *Italic*. **Bold**. ***Bold and italic***.
- [] Unchecked
- [x] Checked

Type: `object`

.. csv-table:: Engine
   :header: "Property", "Type", "Required", "Description"

   :ref:`model <engine-model>`, "`string`", "Required", "Model"
   :ref:`power <engine-power>`, "`integer`", "Required", "Power"
   :ref:`fuel_type <engine-fuel-type>`, "`string`", "Required", "Fuel Type"
   :ref:`turbo <engine-turbo>`, "`boolean`", "Required", "Turbo"
   :ref:`liters <engine-liters>`, "`number`", "Required", "Liters"

----

.. _engine-model:

:ref:`Engine <engine>` > **model**

The name of the engine model.

:Type: `string`
:Required: Required
:Possible Values: Length: `1 <= string <= 100`

----

.. _engine-power:

:ref:`Engine <engine>` > **power**

The power of the engine in HP.

:Type: `integer`
:Required: Required
:Possible Values: integer

----

.. _engine-fuel-type:

:ref:`Engine <engine>` > **fuel_type**

The type of fuel the engine uses.

:Type: `string`
:Required: Required
:Possible Values: `gasoline` `diesel` `electric`

----

.. _engine-turbo:

:ref:`Engine <engine>` > **turbo**

Whether the engine has a turbo or not.

:Type: `boolean`
:Required: Required
:Possible Values: boolean

----

.. _engine-liters:

:ref:`Engine <engine>` > **liters**

The displacement of the engine in liters.

:Type: `number`
:Required: Required
:Possible Values: `0.0 < x`

----

.. _extrapackadvanced:

ExtraPackAdvanced
-----------------
This is the description of the ExtraPack2.

Type: `object`

.. csv-table:: ExtraPackAdvanced
   :header: "Property", "Type", "Required", "Description"

   :ref:`heated_seats <extrapackadvanced-heated-seats>`, "`boolean`", "Optional", "Heated Seats"
   :ref:`heated_steering_wheel <extrapackadvanced-heated-steering-wheel>`, "`boolean`", "Optional", "Heated Steering Wheel"
   :ref:`parking_sensors <extrapackadvanced-parking-sensors>`, "`boolean`", "Optional", "Parking Sensors"
   :ref:`adaptive_cruise_control <extrapackadvanced-adaptive-cruise-control>`, "`boolean`", "Optional", "Adaptive Cruise Control"

----

.. _extrapackadvanced-heated-seats:

:ref:`ExtraPackAdvanced <extrapackadvanced>` > **heated_seats**

Whether the car has heated seats.

:Type: `boolean`
:Required: Optional
:Default: `true`
:Possible Values: boolean

----

.. _extrapackadvanced-heated-steering-wheel:

:ref:`ExtraPackAdvanced <extrapackadvanced>` > **heated_steering_wheel**

Whether the car has a heated steering wheel.

:Type: `boolean`
:Required: Optional
:Default: `true`
:Possible Values: boolean

----

.. _extrapackadvanced-parking-sensors:

:ref:`ExtraPackAdvanced <extrapackadvanced>` > **parking_sensors**

Whether the car has parking sensors.

:Type: `boolean`
:Required: Optional
:Default: `true`
:Possible Values: boolean

----

.. _extrapackadvanced-adaptive-cruise-control:

:ref:`ExtraPackAdvanced <extrapackadvanced>` > **adaptive_cruise_control**

Whether the car has adaptive cruise control

:Type: `boolean`
:Required: Optional
:Default: `true`
:Possible Values: boolean

----

.. _extrapackbasic:

ExtraPackBasic
--------------
This is the description of the ExtraPack1.

Type: `object`

.. csv-table:: ExtraPackBasic
   :header: "Property", "Type", "Required", "Description"

   :ref:`heated_seats <extrapackbasic-heated-seats>`, "`boolean`", "Optional", "Heated Seats"
   :ref:`heated_steering_wheel <extrapackbasic-heated-steering-wheel>`, "`boolean`", "Optional", "Heated Steering Wheel"
   :ref:`parking_sensors <extrapackbasic-parking-sensors>`, "`boolean`", "Optional", "Parking Sensors"

----

.. _extrapackbasic-heated-seats:

:ref:`ExtraPackBasic <extrapackbasic>` > **heated_seats**

Whether the car has heated seats.

:Type: `boolean`
:Required: Optional
:Possible Values: boolean

----

.. _extrapackbasic-heated-steering-wheel:

:ref:`ExtraPackBasic <extrapackbasic>` > **heated_steering_wheel**

Whether the car has a heated steering wheel.

:Type: `boolean`
:Required: Optional
:Possible Values: boolean

----

.. _extrapackbasic-parking-sensors:

:ref:`ExtraPackBasic <extrapackbasic>` > **parking_sensors**

Whether the car has parking sensors.

:Type: `boolean`
:Required: Optional
:Default: `true`
:Possible Values: boolean

----

.. _navigationsystem:

NavigationSystem
----------------
This is the description of the NavigationSystem.

Type: `object`

.. csv-table:: NavigationSystem
   :header: "Property", "Type", "Required", "Description"

   :ref:`type <navigationsystem-type>`, "`string`", "Required", "Type"

----

.. _navigationsystem-type:

:ref:`NavigationSystem <navigationsystem>` > **type**

The type of navigation system.

:Type: `string`
:Required: Required
:Possible Values: `gps` `carplay` `androidauto`

----

.. _upholstery:

Upholstery
----------
This is the description of the Upholstery.

Type: `object`

.. csv-table:: Upholstery
   :header: "Property", "Type", "Required", "Description"

   :ref:`type <upholstery-type>`, "`string`", "Required", "Type"
   :ref:`stitching <upholstery-stitching>`, "`object`", "Required", "Stitching"

----

.. _upholstery-type:

:ref:`Upholstery <upholstery>` > **type**

The type of upholstery.

:Type: `string`
:Required: Required
:Possible Values: `leather` `fabric`

----

.. _upholstery-stitching:

:ref:`Upholstery <upholstery>` > **stitching**

Metadata about the stitching.

:Type: `object`
:Required: Required
:Possible Values: object
