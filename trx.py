#   Python transaction submission to tron network
#   HTTPhash
#   USAGE:          trx.py skey trxaccountaddressstring trxcontractaddresshex hash
#   Requires >= Python3.6, TRON API
#   sudo pip3 install tronapi
import logging, json, sys
from tronapi import Tron

#logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
#logger = logging.getLogger()

full_node = 'https://api.trongrid.io'
solidity_node = 'https://api.trongrid.io'
event_server = 'https://api.trongrid.io/'
private_key = sys.argv[1]
default_address = sys.argv[2]
contract_address = sys.argv[3]
insertHash = sys.argv[4]

tron = Tron(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server,
            private_key=private_key,
            default_address=default_address)

HTTPhash = tron.transaction_builder.trigger_smart_contract(
    contract_address = contract_address,
    function_selector = 'insertHash(string)',
    fee_limit=2000000,
    call_value=0,
    parameters=[
        {'type': 'string', 'value': insertHash}
    ])

sign = tron.trx.sign(HTTPhash["transaction"])
submission = tron.trx.broadcast(sign)
print(submission)
