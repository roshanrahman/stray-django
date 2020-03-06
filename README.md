# Stray Cattle Django - API Documentation

### Base URL

[`https://djangoproject-straycattle.herokuapp.com/`](https://roshanrahman.github.io/stray-django/)

## Quickstart

### Endpoints

The server will respond to the listed API endpoints with the appropriate response. For other endpoints, unlisted or incorrectly used, the server will respond with a `INVALID_ROUTE` response.
|Endpoint|Purpose |
|--|--|
| `auth/` | Handles user authentication (register, login) |
| `reports/`|Handles reports uploaded by citizens (CRUD)|
| `geocoding/`|Handles geocoding operations|
For other URLs, you may receive a `INVALID_ROUTE` response.

## Authentication

**Endpoint**: `/auth`

1. ### New user registration

**Endpoint**: **POST** `/auth/register`

**Parameters** (in POST body):

1. `phone` (required) - User's phone number

2. `password` (required) - User's password

3. `account_type` (optional) - Can be either `citizen` or `authority`

**Example**:

`POST https://djangoproject-straycattle.herokuapp.com/auth/register` with `phone=123`, `password=123` (creates a user with phone number 123, and password 123)

Response:

```json
{
  "data": {
    "jwt": "---jwt_token---",

    "phone": "123",

    "account_type": "citizen"
  },

  "error": null
}
```

1. ### Login

**Endpoint**: **POST** `/auth/login`

**Parameters** (in POST body):

1. `phone` (required) - User's phone number

2. `password` (required) - User's password

**Example**:

`POST https://djangoproject-straycattle.herokuapp.com/auth/login` with `phone=123`, `password=123` (returns user details w/ jwt if user exists)

Response:

```json
{
  "data": {
    "jwt": "---jwt_token---",

    "phone": "123",

    "account_type": "citizen"
  },

  "error": null
}
```
