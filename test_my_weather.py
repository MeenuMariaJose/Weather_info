import pytest
import my_weather

def test_valid_loc():
    api_key = "8c39a1117759d102e76aa34344b125eb"

    output= my_weather.know_your_weather(api_key, "kochi")

    assert "Kochi" in output["Location"]
    assert "temp" in output["weather info"]
    
def test_invalid_loc():
    api_key = "8c39a1117759d102e76aa34344b125eb"
    
    output= my_weather.know_your_weather(api_key, "abc")
    assert "404" in output["cod"]
    assert "city not found" in output["message"]