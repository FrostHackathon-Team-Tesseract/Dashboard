import json 
from web3 import Web3
from .render import Render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core import Paginator
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
public_key = '0xf11Ca215E54f6C27ac385C62FA73A9CcE837CfCA'
private_key = 'e37f0e96eb9535f07d028da356102d0109bc7e33dcfb0518ea899d03d5aa9c5a' 

url = 'https://ropsten.infura.io/v3/7359b2b93d6446b3a60e0801cff91b37'

web3 = Web3(Web3.HTTPProvider(url))

address = web3.toChecksumAddress("0x42CE27Ffb4b5043018543fDFcA8d3f2BF16D5Ab4")
abi = json.loads('''[
	{
		"constant": false,
		"inputs": [
			{
				"name": "rid",
				"type": "uint256"
			},
			{
				"name": "pid",
				"type": "uint256"
			},
			{
				"name": "link",
				"type": "string"
			}
		],
		"name": "add_report",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "fetch_report",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			},
			{
				"name": "",
				"type": "uint256"
			},
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "did",
				"type": "uint256"
			},
			{
				"name": "number",
				"type": "uint256"
			},
			{
				"name": "name",
				"type": "string"
			}
		],
		"name": "add_doctor",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "fetch_doctor",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			},
			{
				"name": "",
				"type": "uint256"
			},
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "patient_info",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			},
			{
				"name": "",
				"type": "uint256"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "pid",
				"type": "uint256"
			},
			{
				"name": "a",
				"type": "uint256"
			},
			{
				"name": "no",
				"type": "uint256"
			},
			{
				"name": "name",
				"type": "string"
			}
		],
		"name": "add_patient",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]''')

contract = web3.eth.contract(address=address,abi=abi)
print(contract)