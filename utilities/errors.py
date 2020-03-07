# General API related errors

INVALID_ROUTE = (
    'INVALID_ROUTE', 'The route you accessed is not a valid route, please check API docs (https://roshanrahman.github.io/stray-django/)'
)

NOT_AUTHORIZED = (
    'NOT_AUTHORIZED', 'You do not have the authorization to access this page. Did you forget JWT?'
)

INVALID_PARAMS = (
    'INVALID_PARAMS', 'The parameters to this request are incorrect/missing. please check API docs (https://roshanrahman.github.io/stray-django/)'
)

SOMETHING_WENT_WRONG = (
    'SOMETHING_WENT_WRONG', 'Something went wrong while processing your request. Internal Server Error'
)

# User Auth specific errors

USER_ALREADY_EXISTS = (
    'USER_ALREADY_EXISTS', 'An account already exists with the phone number you provided'
)
INVALID_PASSWORD = (
    'INVALID_PASSWORD', 'The password you entered is incorrect'
)
USER_DOES_NOT_EXIST = (
    'USER_DOES_NOT_EXIST', 'No account exists with the phone number you provided'
)
