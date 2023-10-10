import requests
import pytest
BASE_URL = "https://dog.ceo/api"


def test_random_dog_img():
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    data = response.json()
    assert data.get('message')

def test_get_rand_dog_img_code():
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    assert response.status_code == 200
    
def test_get_rand_dog_img_link():
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    data = response.json()
    assert data['message'].startswith("https://images.dog.ceo")

def test_is_random_fifth():
	response = requests.get(f"{BASE_URL}/breeds/image/random/3")
	data = response.json()
	assert len(data['message']) == 5
     
def test_list():
	response = requests.get(f"{BASE_URL}/breeds/list/all")
	data = response.json()
	assert len(data["message"]) > 0
     
