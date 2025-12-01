```
Andrey Obukhov
Harvard's CS50 SQL August 2024
Final Project
```
# Design Document

Video overview: https://www.youtube.com/watch?v=yusyZcxugCs

## Scope

The database for CS50 SQL includes main entities necessary to operate some generic food market. As such, included in the database's scope is:

* Items, including any possible products food market can deal with, the time at which the particular item arrived to the storehouse
* Expirations, including expiration date for any particular item
* Quantities, including current quantity for any particular item with units used in calculation
* Countries, from which items arrived
* Suppliers, including the list of companies market operates with

Out of scope are elements like market employees, physical stores, document flow and accounting details.

## Functional Requirements

This database will support:

* CRUD operations for food market items
* Tracking present and past suppliers and countries they are delivering goods from

Note that in this iteration, the system will not support any items prices management.

## Representation

Entities are captured in SQLite tables with the following schema.

### Entities

The database includes the following entities:

#### Countries

The `countries` table includes:

* `id`, which specifies the unique ID for the particular country as an `INTEGER`. This column thus has the `PRIMARY KEY` constraint applied.
* `name`, which specifies the country's name as `TEXT`.

Column `name` in the `countries` table is required and hence should have the `NOT NULL` constraint applied. No other constraints are necessary.

#### Suppliers

The `suppliers` table includes:

* `id`, which specifies the unique ID for the supplier as an `INTEGER`. This column thus has the `PRIMARY KEY` constraint applied.
* `name`, which is the supplier's company name as `TEXT`.
* `from`, which is the timestamp at which the first delivery from this current suppliers occured. The default value for the `from` attribute is the current timestamp, as denoted by `DEFAULT CURRENT_TIMESTAMP`. Also there is `NOT NULL` constraint.
* `country_id` which is the `INTEGER` ID of the country from which current supplier cames from. This column thus has the `FOREIGN KEY` constraint applied, referencing the `id` column in the `countries` table to ensure data integrity.

All columns are required and hence have the `NOT NULL` constraint applied where a `PRIMARY KEY` or `FOREIGN KEY` constraint is not.

#### Items

The `items` table includes:

* `id`, which specifies the unique ID for the item (a.k.a product on the food market) as an `INTEGER`. This column thus has the `PRIMARY KEY` constraint applied.
* `name`, which specifies the item's title as `TEXT`, given `TEXT` is appropriate for name fields. A `NOT NULL` constraint ensures that there will not be item without any discription.
* `arrived`, which specifies the date current items was delivered to the storehouse. Timestamps in SQLite can be conveniently stored as `NUMERIC`, per SQLite documentation at <https://www.sqlite.org/datatype3.html>. The default value for the `from` attribute is the current timestamp, as denoted by `DEFAULT CURRENT_TIMESTAMP`. Also there is `NOT NULL` constraint.
* `sup_id`, which is the ID of the supplier who delivered the item as an `INTEGER`. This column thus has the `FOREIGN KEY` constraint applied, referencing the `id` column in the `suppliers` table to ensure data integrity.

Columns `name` and `arrived` in the `items` table are required and hence should have the `NOT NULL` constraint applied. No other constraints are necessary.

#### Expirations

The `expirations` table includes:

* `id`, which specifies the unique ID for the expiration date as an `INTEGER`. This column thus has the `PRIMARY KEY` constraint applied.
* `date`, which is the timestamp for expiration date for particular item.
* `item_id` which is the ID of the item as an `INTEGER`. This column thus has the `FOREIGN KEY` constraint applied, referencing the `id` column in the `items` table to ensure data integrity.

Column `date` in the `expirations` table is required and hence should have the `NOT NULL` constraint applied. No other constraints are necessary.

#### Quantities

The `quantities` table includes:

* `id`, which specifies the unique ID for the expiration date as an `INTEGER`. This column thus has the `PRIMARY KEY` constraint applied.
* `quantity`, which is the exact `INTEGER` quantity of particular items in prescribed units.
* `units`, which is the `TEXT` quantity units.
* `item_id` which is the ID of the item as an `INTEGER`. This column thus has the `FOREIGN KEY` constraint applied, referencing the `id` column in the `items` table to ensure data integrity.

All columns are required and hence have the `NOT NULL` constraint applied where a `PRIMARY KEY` or `FOREIGN KEY` constraint is not.

### Relationships

The below entity relationship diagram describes the relationships among the entities in the database.

![ER Diagram](diagram.png)

As detailed by the diagram:

* One item has one and only prescribed expiration date. Similarly, one expiration date is associated with one and only one row in the `items` table.
* One item has one and only quantity information. Similarly, one quanity is associated with one and only one row in the itens table.
* One supplier is associated with one to many items. For the date saving puproses, we do not containing information about past or perspective suppliers with zero item in the table. One item is associated with one to many suppliers. There is not item without any supplier.
* Supplier is associated with one and only one origin country. If one supplier company operates internationally, we provide more than one row in `suppliers` table. One country is associated with one to many suppliers.

## Optimizations

Per the typical queries in `queries.sql`, it is common for users of the database to access all items with expiration dates and quantities in one table. For that reason, there is view `products` with those three tables joined.

Also indexes are created on the `name`s in `items`, `countries` and `suppliers` tables to speed up string search.

## Limitations

As was mentioned before, we do not consider employees, physical stores, document flow and accounting details. Thus, this database do not pretend to be all-purpose storage.
