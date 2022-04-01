import os
import pathlib
import socket


USER_DIR = str(pathlib.Path.home())
CHAINPROX_DIR_NAME = '.chainprox'
CHAINPROX_CONFIG_NAME = 'chainprox.cfg'
CHAINPROX_DIR = os.path.join(USER_DIR, CHAINPROX_DIR_NAME)

if not os.path.exists(CHAINPROX_DIR):
    os.mkdir(CHAINPROX_DIR)


PROCESSOR_LOCAL_PORT = 8090

PROXY_LISTENER_LOCAL_PORT = 8080
DOMAIN = 'chainprox.com'
DOMAIN_IP = socket.gethostbyname(DOMAIN)

# The listener server which handle local connection and proxies them.
PROXY_LISTENER_SERVER_IP, PROXY_LISTENER_SERVER_PORT = DOMAIN_IP, 10014

# The port where proxy listening incoming connection for fetching
# and return to proxy engine.
PROXY_FETCHER_LOCAL_PORT = 8090

# The server with job to fetching (connected by domestic proxies).
PROXY_FETCHER_SERVER_IP, PROXY_FETCHER_SERVER_PORT = DOMAIN_IP, 10012

PROXY_SSL_ENABLED = True

# The proxy engine management server.
PROXY_MNG_SERVER_IP, PROXY_MNG_SERVER_PORT = DOMAIN_IP, 10010

# These variables will be filled with env-vars values or conf files:
PUBLIC_KEY = None
SECRET_KEY = None
SECRET_KEY_FILE = None
