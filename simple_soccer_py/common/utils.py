def clamp(arg: float, min_val: float, max_val: float) -> float:
    """clamps the first argument between the second two"""
    if min_val >= max_val:
        raise ValueError("<Clamp>MaxVal < MinVal!")
    return max(min_val, min(arg, max_val))
