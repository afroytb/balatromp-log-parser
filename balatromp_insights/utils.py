from pydantic import ValidationError


def raise_if_none[T](val: T | None) -> T:
    if val is None:
        raise ValidationError(f"{val} is None. Parsing Error.")
    return val

