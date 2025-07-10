def test_login_fail(client):
    resp = client.post("/auth/login", json={"username": "no", "password": "no"})
    assert resp.status_code == 401
