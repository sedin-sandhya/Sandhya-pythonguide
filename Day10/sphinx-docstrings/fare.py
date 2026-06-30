def calculate_fare(distance: float, vehicle: str) -> float:
    """
    Calculate cab fare based on distance and vehicle type.

    Args:
        distance (float):
            Distance travelled in kilometers.

        vehicle (str):
            Type of vehicle.
            Allowed values:
            "car", "bike", "auto".

    Returns:
        float:
            Final fare amount in Indian Rupees.

    Raises:
        ValueError:
            If vehicle type is not supported.

    Example:
        >>> calculate_fare(10.0, "car")
        200.0

        >>> calculate_fare(5.0, "bike")
        50.0
    """

    rates = {
        "car": 20,
        "bike": 10,
        "auto": 15
    }


    if vehicle not in rates:
        raise ValueError("Unsupported vehicle")


    return distance * rates[vehicle]



def apply_discount(fare: float, discount: float) -> float:
    """
    Apply discount percentage to fare.

    Args:
        fare (float):
            Original fare amount.

        discount (float):
            Discount percentage.

    Returns:
        float:
            Fare after applying discount.

    Raises:
        ValueError:
            If discount is greater than 100.

    Example:
        >>> apply_discount(200.0, 10)
        180.0

        >>> apply_discount(500.0, 20)
        400.0
    """


    if discount > 100:
        raise ValueError("Invalid discount")


    return fare - (fare * discount / 100)

def main():
    print(calculate_fare(10.0, "car"))

if __name__ == "__main__":
    main()