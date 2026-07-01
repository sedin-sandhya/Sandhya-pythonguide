# Pydantic BaseModel with Field() constraints (ge, le, min_length, min_items). 
# PaymentMethod uses Enum for restricted values. 
# A custom @validator checks that order total > 0. 
# ValidationError gives structured JSON error messages. 
# This is exactly how FastAPI validates every request body -- 
# mastering Pydantic means mastering FastAPI.
# Food order validation using Pydantic. 
# Structured error messages on invalid input. 


from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import List, Optional
from enum import Enum

class PaymentMethod(str, Enum):

    UPI = "upi"
    CARD = "card"
    CASH = "cash"

class OrderItem(BaseModel):

    name : str = Field(
        ...,
        min_length = 1,
        max_length = 100
    )

    quantity : int = Field(
        ...,
        ge = 1,
        le = 20
    )

    price : float = Field(
        ...,
        ge = 0
    )

class Order(BaseModel):

    customer_name : str = Field(
        ...,
        min_length = 2
    )

    items : List[OrderItem] = Field(
        ...,
        min_length = 1
    )

    delivery_address : str = Field(
        ...,
        min_length = 10
    )

    payment_method: PaymentMethod

    tip : Optional[float] = Field(
        None,
        ge = 0,
        le = 500
    )

    @field_validator("items")
    def total_must_be_positive(cls, items):

        total = sum(
            item.price * item.quantity
            for item in items
        )


        if total <= 0:
            raise ValueError(
                "Order total must be greater than 0"
            )

        return items

def main():

    try:

        order = Order(
            customer_name = "Sandhya",

            items = [
                OrderItem(
                    name = "Burger",
                    quantity = 2,
                    price = 150
                ),

                OrderItem(
                    name = "Pizza",
                    quantity = 1,
                    price = 300
                )
            ],

            delivery_address = "Chennai Anna Nagar Kora",

            payment_method = "upi",


        )

        print(order)

        print("\nTotal:")

        total = sum(
            item.price * item.quantity
            for item in order.items
        )
        print(total)

        if order.tip != None:
            print("\n Tip:")
            print(order.tip)

    except ValidationError as e:

        print(e.json())

if __name__ == "__main__":
    main()