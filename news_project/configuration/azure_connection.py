import os
import sys
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from news_project.exception import ArticleException
from news_project.logger import logging
# account_name : 'newsarticlestorage'
# container_name : 'newsarticlecontainer' 


class BlobClient:
    def __init__(self):
        """
        Initialize Azure Blob Client with Azure credentials.
        """
        try:
            self.azure_client_id = os.getenv('AZURE_CLIENT_ID')
            self.azure_tenant_id = os.getenv('AZURE_TENANT_ID')
            self.azure_client_secret = os.getenv('AZURE_CLIENT_SECRET')
            self.azure_secret_name = os.getenv('AZURE_SECRET_NAME')
            self.azure_storage_url = os.getenv('AZURE_STORAGE_URL')
                        

                # create a credential object
            self.credentials = ClientSecretCredential(
                    client_id = self.azure_client_id,
                    client_secret = self.azure_client_secret,
                    tenant_id = self.azure_tenant_id
                    )
            logging.info("Azure Blob Client initialization successful")
        except Exception as e:
            raise ArticleException(e, sys) from e


    def get_binary_blob_data(self, container_name, blob_name):
        """
        Downloads the specified blob from the Azure Blob Storage container.
        
        Arguments:
        container_name : name of the Azure Blob Storage container
        blob_name      : name of the blob(filename) to be downloaded
        """        
        try:
            # set client to access azure storage container
            blob_service_client = BlobServiceClient(account_url= self.azure_storage_url, credential= self.credentials)

            # get the container client 
            container_client = blob_service_client.get_container_client(container=container_name)

            # download blob data 
            blob_client = container_client.get_blob_client(blob= blob_name)
            print(blob_name)
            binary_data = blob_client.download_blob().readall()
            print("________________________________________________________________here")
            return binary_data
        except Exception as e:
            raise ArticleException(e, sys) from e


    def list_blob(self, container_name):
        """
        Lists all blobs in the specified Azure Blob Storage container.
        
        Arguments:
        container_name : name of the Azure Blob Storage container
        """
        try:     
            # set client to access azure storage container
            blob_service_client = BlobServiceClient(account_url= self.azure_storage_url, credential= self.credentials)

            # get the container client 
            container_client = blob_service_client.get_container_client(container=container_name)

            for blob in container_client.list_blobs():
                return blob.name
        except Exception as e:
            raise ArticleException(e, sys) from e

    def get_multi_blob_data(self, container_name):
        """
        Downloads all blobs in the specified Azure Blob Storage container.
        
        Arguments:
        container_name : name of the Azure Blob Storage container
        """
        try:

            # set client to access azure storage container
            blob_service_client = BlobServiceClient(account_url= self.azure_storage_url, credential= self.credentials)

            # get the container client 
            container_client = blob_service_client.get_container_client(container=container_name)

            for blob in container_client.list_blobs():
                blob_client = container_client.get_blob_client(blob= blob.name)
                data = blob_client.download_blob().readall()
                return data.decode("utf-8")
        except Exception as e:
            raise ArticleException(e, sys) from e


    def upload_blob(self, local_dir, container_name):
        """
        Uploads all files from the specified local directory to the specified Azure Blob Storage container.
        
        Arguments:
        local_dir      : local directory path
        container_name : name of the Azure Blob Storage container
        """
        try:
            # set client to access azure storage container
            blob_service_client = BlobServiceClient(account_url= self.azure_storage_url, credential= self.credentials)

            # get the container client 
            container_client = blob_service_client.get_container_client(container=container_name)

            # read all files from directory
            filenames = os.listdir(local_dir)
                
            for filename in filenames :
                # get full file path
                full_file_path = os.path.join(local_dir, filename) 

                # read files and upload data to blob storage container 
                with open(full_file_path, "rb") as fl :
                        data = fl.read()
                        container_client.upload_blob(name= filename, data=data, overwrite=True)

            logging.info("Blobs uploaded successfully")
        except Exception as e:
            raise ArticleException(e, sys) from e





# client = BlobClient()
# client.upload_blob('logs', 'newsarticlecontainer')
