# API Constants - configured for use with Bumper self-hosted server
# Bumper intercepts DNS for *.ecouser.net and *.ecovacs.com domains,
# redirecting them to your local Bumper server IP (BUMPER_ANNOUNCE_IP).
# See: https://github.com/MVladislav/bumper

# Credentials matching the Ecovacs API (same as sucks/bmartin5692 sucks fork)
API_CLIENT_KEY = "eJUWrzRv34qFSaYk"
API_SECRET = "Cyu5jcR4zyK6QEPn1hdIGXB5QIDAQABMA0GC"
API_PUBLIC_KEY = 'MIIB/TCCAWYCCQDJ7TMYJFzqYDANBgkqhkiG9w0BAQUFADBCMQswCQYDVQQGEwJjbjEVMBMGA1UEBwwMRGVmYXVsdCBDaXR5MRwwGgYDVQQKDBNEZWZhdWx0IENvbXBhbnkgTHRkMCAXDTE3MDUwOTA1MTkxMFoYDzIxMTcwNDE1MDUxOTEwWjBCMQswCQYDVQQGEwJjbjEVMBMGA1UEBwwMRGVmYXVsdCBDaXR5MRwwGgYDVQQKDBNEZWZhdWx0IENvbXBhbnkgTHRkMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDb8V0OYUGP3Fs63E1gJzJh+7iqeymjFUKJUqSD60nhWReZ+Fg3tZvKKqgNcgl7EGXp1yNifJKUNC/SedFG1IJRh5hBeDMGq0m0RQYDpf9l0umqYURpJ5fmfvH/gjfHe3Eg/NTLm7QEa0a0Il2t3Cyu5jcR4zyK6QEPn1hdIGXB5QIDAQABMA0GCSqGSIb3DQEBBQUAA4GBANhIMT0+IyJa9SU8AEyaWZZmT2KEYrjakuadOvlkn3vFdhpvNpnnXiL+cyWy2oU1Q9MAdCTiOPfXmAQt8zIvP2JC8j6yRTcxJCvBwORDyv/uBtXFxBPEC6MDfzU2gKAaHeeJUWrzRv34qFSaYkYta8canK+PSInylQTjJK9VqmjQ'

# URL formats - domains stay the same; Bumper intercepts them via DNS override.
# eco-{country}-api.ecovacs.com  -> used for login (intercepted by Bumper)
# users-{continent}.ecouser.net  -> Bumper serves on port 8007
# portal-{continent}.ecouser.net -> Bumper serves on port 443
API_MAIN_URL_FORMAT = 'https://eco-{country}-api.ecovacs.com/v1/private/{country}/{lang}/{deviceId}/{appCode}/{appVersion}/{channel}/{deviceType}'
API_USER_URL_FORMAT = 'https://users-{continent}.ecouser.net:8007/user.do'
API_PORTAL_URL_FORMAT = 'https://portal-{continent}.ecouser.net/api'
API_USERSAPI = 'users/user.do'
API_IOTDEVMANAGERAPI = 'iot/devmanager.do'
API_PRODUCTAPI = 'pim/product'
API_REALM = 'ecouser.net'