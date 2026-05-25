Overview
This project prepares and cleans an e-commerce dataset for analysis.
The goal is to remove duplicates, handle missing values, standardize text, and verify data integrity.

Steps
Converted text fields to lowercase and stripped spaces.

Standardized dates to ISO format.

Imputed missing values (median for UnitPrice, mean for Quantity, "No Coupon" for CouponCode).

Replaced inconsistent text values (online to credit_card).

Removed duplicates based on CustomerID and TrackingNumber.

Filtered invalid values (Quantity between 0–100, prices > 0).

Rounded numeric fields to 2 decimal places.

Verification Gate
No duplicate OrderID or TrackingNumber.

All dates valid ISO format.
