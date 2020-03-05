# Stray Cattle Django - API Documentation

### Base URL

`https://djangoproject-straycattle.herokuapp.com/`

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

   Result:

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


    __Example__:

    `POST https://djangoproject-straycattle.herokuapp.com/auth/login` with `phone=123`, `password=123` (returns user details w/ jwt if user exists)

    Result:
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
