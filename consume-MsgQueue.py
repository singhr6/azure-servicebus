import yaml
from azure.servicebus import ServiceBusClient, ServiceBusMessage

config_file='c:\\temp\\azure-servicebus.yaml'

# load confile file
stream = open(config_file, 'r')
docs = yaml.load_all(stream, Loader=yaml.FullLoader)

# initialize variable from yaml file
for doc in docs:
    for k, v in doc.items():
        if k == 'connection-string':
             connection_string= v
        if k == 'queue-name':
            queue_name=v


# intialize client for service bus
servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_string, logging_enable=True)


# start a consumer for queue
with servicebus_client:
    receiver = servicebus_client.get_queue_receiver(queue_name=queue_name)
    with receiver:
        for msg in receiver:
            print("Received: " + str(msg))
            receiver.complete_message(msg)
            #receiver.receive_messages(max_message_count=10)

