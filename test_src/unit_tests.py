import unittest
from pathlib import Path
from . import cli, runner
import ipfs_wrapper as ipfs

class TestClass(unittest.TestCase):
    
    def test_consumer(self,hash,path: Path):
        ipfs.retrieve(hash,path)
        self.assertEqual(Path.path.isdir(path + "/" + hash) , True, "Não foi criado o diretório.")
    
    def test_serve(self,path: Path):
        self.assertEqual(ipfs.serve(path) , True, "O diretório não foi adicionado ao IPFS.")

    def test_ipfsclient_serveDir(self,path: Path):
        
        self.assertEqual(ipfs.ipfsClient.serveDir(path), True, "O diretório não foi adicionado ao IPFS.")
    
    def test_ipfsclient_serveFile(self,path: Path):     
        self.assertEqual(ipfs.ipfsClient.serveFile(path) , True, "O arquivo não foi adicionado ao IPFS.")

    def test_runner_Add(self,path: Path):     
        self.assertEqual(runner.add(path) , True, "O arquivo não foi adicionado ao IPFS.")
    
    def test_runner_retrieve(self,hash,path: Path):
        runner.get(hash,path)    
        self.assertEqual(Path.path.isdir(path + "/" + hash) , True, "Não foi criado o diretório.")


if __name__ == "__main__":
            unittest.main()
