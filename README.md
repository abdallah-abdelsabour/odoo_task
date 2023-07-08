# Purchase Request Cycle Solution

## Task
You are required to create a module that integrates with Odoo purchase module. The module will provide functionality for requesting purchase orders and approving them before purchase orders are created. 

## Task Details
**Purchase Request module**
1. Create a new model called "Purchase Request".
2. Add a new menu item "Purchase Requests" to the purchase module.
3. The purchase request form should include the following fields:
   - **State**: Contains two states, "Draft" and "Confirmed".
   - **Analytical Account**: Related field to the analytical account model.
   - **Creation Date**: Automatically set and read-only (cannot be modified in any state).
   - **Created By**: Automatically set and read-only (cannot be modified in any state).
   - **Requested By**: Related field to the user model. Initially set to the user creating the record, but can be manually modified to select another user.
   - **Requested On**: Date field that the user can select manually. It should have a default value of the creation date.
   - **Purchase Request Lines**: One2many field for adding multiple lines to the purchase request. Each line should contain the following fields:
     - **Product**: Related field to the product model.
     - **Vendor**: Related field to the res partner model.
     - **Quantity**: Float field for specifying the quantity.
     - **UOM**: Related field to the uom.uom model, with a domain based on the product's defined unit of measure (see purchase order line model).

4. When confirming the purchase request, the system should loop through the purchase request lines, group them by vendor, and create a draft purchase order (RFQ) for each group of lines related to the same vendor.
5. After confirmation, all fields in the purchase request, including the lines, should be set as read-only.
6. Each purchase order should have a smart tab for the related purchase request.
7. In the purchase request smart tab, display the purchase orders created from it.

**Hint:** Take inspiration from the Odoo purchase order and purchase order line models when creating the purchase request and purchase request line models.
