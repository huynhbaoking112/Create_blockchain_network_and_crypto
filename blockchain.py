import hashlib
from datetime import datetime, timedelta

class Block:
    def __init__(self, data):
        self.data = data
        self.hash = ""
        self.nonce = 0
        self.prev_hash = ""
        self.total_time = 0

def hash(block):

    data =  block.data + block.prev_hash + str(block.nonce)
    data = data.encode('utf-8')
        
    return hashlib.sha256(data).hexdigest()
    

class Blockchain:
    
    def __init__(self):
        self.chain = []

        block = Block("Geneis Block")
        block.hash = hash(block)
        self.chain.append(block)
    
    def add_block(self,data):
        block = Block(data)
        block.prev_hash = self.chain[-1].hash

        start = datetime.now()
        while hash(block).startswith("000000") == False:
            block.nonce+=1
        end = datetime.now()
        block.hash = hash(block)
        block.total_time = str(end-start)
        self.chain.append(block)

    def print(self):
        for block in self.chain:
            print("Data: ", block.data)
            print("Hash: ", block.hash)
            print("Prev_Hash: ", block.prev_hash)
            print("Nonce: ",block.nonce)
            print("Time create: ", block.total_time)
            print("") 

    def is_Valid(self):
        for i in range(0, len(self.chain)-1):
            if hash(self.chain[i]) != self.chain[i+1].prev_hash:
                print("The string is changed ")
                print(self.chain[i].data)
                print(i)
                break
        

blockchain = Blockchain()
blockchain.add_block("King Huynh")
blockchain.add_block("King Huynh2")
blockchain.add_block("King Huynh3")

# blockchain.chain[2].data = "Thay"

# blockchain.is_Valid()



blockchain.print()