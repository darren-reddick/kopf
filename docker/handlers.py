import kopf
import kubernetes
import yaml

# This is placeholder code - will only run if the testing.org/v1 custom resource definition has been created
@kopf.on.create('testing.org', 'v1', 'custom')
def create_fn(body, **kwargs):
    print(f"A handler is called with body: {body}")
