# Stray Cattle Django - API Documentation

### Base URL

[`https://djangoproject-straycattle.herokuapp.com/`](http://djangoproject-straycattle.herokuapp.com/)

## Quickstart

### Endpoints

The server will respond to the listed API endpoints with the appropriate response. For other endpoints, unlisted or incorrectly used, the server will respond with a `INVALID_ROUTE` response.

| Endpoint     | Purpose                                       |
| ------------ | --------------------------------------------- |
| `auth/`      | Handles user authentication (register, login) |
| `reports/`   | Handles reports uploaded by citizens (CRUD)   |
| `geocoding/` | Handles geocoding operations                  |

For other URLs, you may receive a `INVALID_ROUTE` response.

### Passing JWT Token

User-specific actions will require JWT Authorization. To pass JWT to the request,
send the JWT token in the request's header, like this:

`'authorization': 'Bearer <---jwt---->'`

Example:

```json
{
  "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjoyfQ.j7fLGPF4VOS4uGUP6hgKTPkAHPcEz3WrVvg1RYNWZI4"
}
```

(in the request's header)

## Authentication

**Endpoints**:

| Endpoint | Purpose |
| -----| ----- |
| `auth/register` | Create a new account |
| `auth/login` | Login to an account |


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

2. ### Login

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

## Reports

1. ### Add a report

**Endpoint**: **POST** `/reports/add` (**User must be authenticated with JWT**)

**Parameters** (in POST body):

1. `latitude` (required) - Latitude in decimal

2. `longitude` (required) - Longitude in decimal

3. `images` (required) - List (array) of URLs (in JSON-encoded string format)

**Example**:

`POST https://djangoproject-straycattle.herokuapp.com/reports/add`

with:

Header containing:

`Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjoyfQ.j7fLGPF4VOS4uGUP6hgKTPkAHPcEz3WrVvg1RYNWZI4`

Body containing:

`latitude=0` & `longitude=0` & `images=['http://images.gg.com/445.jpg','http://example.image.org/2334.jpg']` (returns success message if report is added)

Response:

```json
{
  "data": {
    "success": true,
    "action_name": "ADD_REPORT"
  },
  "error": null
}
```
