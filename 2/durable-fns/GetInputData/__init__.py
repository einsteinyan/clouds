# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging, os

from azure.storage.blob import BlobServiceClient

connect_str = "DefaultEndpointsProtocol=https;AccountName=cloudsfn;AccountKey=DUxGyO3gFIev01oujcLaOiYXiHiEKhROfvLMMdjsPqS1A8ZJ+3GLpGKMWBI33guMWplQHyYUAZT/+AStZXkyEg==;EndpointSuffix=core.windows.net"

def main(name: str) -> list:
    output = list()

    local_path = "./data"
    #Download the files from the blob storage
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_client = blob_service_client.get_container_client(container="input-data")
        blob_list = container_client.list_blobs()

        for blob in blob_list:
            local_file_name = blob.name
            download_file_path = os.path.join(local_path, local_file_name)
            with open(file=download_file_path, mode="wb") as download_file:
                download_file.write(container_client.download_blob(blob.name).readall())
    except Exception as ex:
        logging.error(ex)
    
    #Process the downloaded files
    files=["mrinput-1.txt", "mrinput-2.txt", "mrinput-3.txt", "mrinput-4.txt"]
    for file in files:
        fileObj = open(os.path.join(local_path, file), 'r')
        lines = fileObj.readlines()
        count = 0
        for line in lines:
            output.append((count, line.replace("\n", "")))
            count += 1

    return output

