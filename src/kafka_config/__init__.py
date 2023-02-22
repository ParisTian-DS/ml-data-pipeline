
import os

#cloud api details

API_KEY = "3YGEQUWKQUYG4RBA"
API_SECRET_KEY = "oW1FECG5o6o1xZ33PGJchwEA3tJBORBC8C1/iIWV+Y48KRDDw3kT/E95IyrJt0v7"
BOOTSTRAP_SERVER = "pkc-4nxnd.asia-east2.gcp.confluent.cloud:9092"
#API_KEY = os.getenv('API_KEY',None)
#API_SECRET_KEY = os.getenv('API_SECRET_KEY',None)
#BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER',None)
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)

SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"

# Schema related variables
SCHEMA_REGISTRY_API_KEY = "4FFGJ56WYBQGC3BU"
SCHEMA_REGISTRY_API_SECRET = "AwvHO0xheroMWK4rbTTF1ywxxcXUd/SyEFWNcBwWAvaGjRsPQZUhP3TkfTvByP9O"
ENDPOINT_SCHEMA_URL  = "https://psrc-8kz20.us-east-2.aws.confluent.cloud"


#SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY',None)
#SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET',None)
#ENDPOINT_SCHEMA_URL  = os.getenv('ENDPOINT_SCHEMA_URL',None)

def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

