from sys import path
import ipfshttpclient
from ipfshttpclient import exceptions
from ipfshttpclient import client
from ipfshttpclient.utils import F
from pathlib import Path


class ipfsClient:

    def __init__(self):
        try:
            self._client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001")
        except exceptions.AddressError:
            print("Invalid MultiAddress: Please enter a valid Address. For more information see: https://github.com/ipfs/go-ipfs/blob/master/docs/config.md#addresses")
        except exceptions.ConnectionError:
            print("Connection Error: Failed to connect with IPFS. Please verify Ipfs address and if IPFS is running ")
        except exceptions.VersionMismatch:
            print("IPFS version is not compatible, see more information in: https://github.com/ipfs-shipyard/py-ipfs-http-client")

    def serveFile(self,path: Path)-> str:
        try:
            res = self._client.add(path)
            return res[-1].get('Hash')
        except exceptions.EncodingError:
            print("Failed to encode data. Please verify the input data.")
            
    def serveDir(self,path: Path)-> str:
        try:
            res = self._client.add(path,recursive=True)
            return res[-1].get('Hash')
        except exceptions.EncodingError:
            print("Failed to encode data. Please verify the input data.")

    def consume(self,hash,destination:Path):
        try:
            self._client.get(hash,destination)
        except exceptions.StatusError:
            print("Bad request. Request failed, daemon responds with an error to our request.")

    def close(self):  # Call this when your done
	    self._client.close()

