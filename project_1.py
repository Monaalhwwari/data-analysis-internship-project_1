import pandas as pd
import numpy as np
import openpyxl

df = pd.read_excel("Dataset for Data Analytics.xlsx")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

df.columns = df.columns.str.strip()

df["Date"]=pd.to_datetime(df["Date"])

df["CustomerID"]=df["CustomerID"].astype(str).str.strip().str.lower()

df["Product"]=df["Product"].astype(str).str.strip().str.lower()

df["Quantity"]=pd.to_numeric(df["Quantity"])

df["UnitPrice"]=pd.to_numeric(df["UnitPrice"])

df["ShippingAddress"]=df["ShippingAddress"].astype(str).str.strip().str.lower()

df["PaymentMethod"]=df["PaymentMethod"].astype(str).str.strip().str.lower()

df["OrderStatus"]=df["OrderStatus"].astype(str).str.strip().str.lower()

df["TrackingNumber"]=df["TrackingNumber"].astype(str).str.strip().str.lower()

df["ItemsInCart"]=pd.to_numeric(df["ItemsInCart"])

df["CouponCode"]=df["CouponCode"].astype(str).str.strip().str.lower()

df["ReferralSource"]=df["ReferralSource"].astype(str).str.strip().str.lower()

df["TotalPrice"]=pd.to_numeric(df["TotalPrice"])

df["UnitPrice"] = df["UnitPrice"].fillna(df["UnitPrice"].median())

df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())

df["CouponCode"]=df["CouponCode"].fillna("No Coupon")

columns = ["CustomerID","Product","ShippingAddress","TrackingNumber",
        "PaymentMethod","OrderStatus","CouponCode","ReferralSource"]

df[columns] = df[columns].apply(lambda x: x.str.replace(" ", "_"))

df["PaymentMethod"] = df["PaymentMethod"].str.replace("online", "credit_card")

df=df.drop_duplicates(["CustomerID","TrackingNumber"])

df=df[df["Quantity"].between(0,100)]

df=df[df["UnitPrice"] > 0]

df=df[df["TotalPrice"] > 0]

df["UnitPrice"] = df["UnitPrice"].round(2)
df["TotalPrice"] = df["TotalPrice"].round(2)

if df["OrderID"].nunique() == len(df):
    print("Passed: No duplicate in OrderID")
else:
    print("Failed: Duplicate in OrderID found")

if df["TrackingNumber"].nunique() == len(df):
    print("Passed: No duplicate in TrackingNumber")
else:
    print("Failed: Duplicate in TrackingNumber found")

if df["Date"].dt.strftime("%Y-%m-%d").isnull().sum() == 0:
    print("Passed: All dates are in ISO format")
else:
    print("Failed: Date format issues found")