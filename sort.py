def sort(
        width: float, 
        height: float, 
        length:float, 
        mass:float
    ) -> str:
    # Calculate the volume
    volume = width * height * length
    
    # Check if the package is bulky
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    
    # Check if the package is heavy
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"