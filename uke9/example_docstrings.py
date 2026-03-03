def request_tide_info_numpy(latitude: float, longitude: float) -> str:
    """Request tide information from the API.

    Parameters
    ----------
    latitude : float
        Latitude of the location (decimal degrees).
    longitude : float
        Longitude of the location (decimal degrees). Example: A long line of
        text is wrapped with the same indent as above.

    Returns
    -------
    str
        The raw XML response from the tide API.
    """
    return ""


def request_tide_info_google(latitude: float, longitude: float) -> str:
    """Request tide information from the API.

    Args:
        latitude (float): Latitude of the location (decimal degrees).
        longitude (float): Longitude of the location (decimal degrees). Example: A
            long line of text is wrapped with an extra indent.

    Returns:
        str: The raw XML response from the tide API.
    """
    return ""


if __name__ == "__main__":
    # Demonstrate pop-ups for docstrings
    print(request_tide_info_numpy(59.91, 10.75))
    print(request_tide_info_google(59.91, 10.75))
