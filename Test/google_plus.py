# Credentials you get from registering a new application
client_id = 'ididididid.apps.googleusercontent.com'
client_secret = 'secret'
redirect_uri = 'https://github.com/'

# OAuth endpoints given in the Google API documentation
authorization_base_url = "https://accounts.google.com/o/oauth2/auth"
token_url = "https://accounts.google.com/o/oauth2/token"
scope = [ "https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile" ]

from requests_oauthlib import OAuth2Session
google = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

# Redirect user to Google for authorization
authorization_url, state = google.authorization_url(authorization_base_url, access_type="offline", approval_prompt="force")
print 'Please go here and authorize,', authorization_url

# Get the authorization verifier code from the callback url
redirect_response = raw_input('Paste the full redirect URL here:')

# Fetch the access token
google.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)

# Fetch a protected resource, i.e. user profile
r = google.get('https://www.googleapis.com/oauth2/v1/userinfo')
print r.content
