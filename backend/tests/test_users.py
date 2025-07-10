def test_users_unauth(client):
    resp = client.get("/users/")
    assert resp.status_code == 401
