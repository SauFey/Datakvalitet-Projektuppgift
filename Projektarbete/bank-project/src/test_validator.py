import pytest
import pandas as pd
from etl.validate import validate_row, validate_data

# Exempel på giltig rad
valid_row = {
    "Customer": "Anna Andersson",
    "Address": "Ringstigen 91, 55006 Varberg",
    "Phone": "08-11 67 41",
    "Personnummer": "551226-2535"
}

# Exempel på ogiltig rad
invalid_row = {
    "Customer": "",
    "Address": "",
    "Phone": "12345",
    "Personnummer": "ABC123"
}

def test_validate_row_valid():
    is_valid, reason = validate_row(valid_row)
    assert is_valid is True
    assert reason is None

def test_validate_row_invalid():
    is_valid, reason = validate_row(invalid_row)
    assert is_valid is False
    assert isinstance(reason, str)
    assert "saknas" in reason or "ogiltigt" in reason.lower()

def test_validate_data():
    df = pd.DataFrame([valid_row, invalid_row])
    valida, ogiltiga, felorsaker = validate_data(df)
    assert len(valida) == 1
    assert len(ogiltiga) == 1
    assert len(felorsaker) == 1
    assert isinstance(felorsaker[0], str)
