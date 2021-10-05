# This program simulates a mock blockchain for a proof of concept only.
# To run this program, use your terminal (cmd on Windows)
#
# Here, we create transactions, validate blocks and construct a mock
# blockchain. We also start a server that will allow us to query the
# blockchain after it is populated.
#
# This software is inspired by the version found here:
# https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/
#
# Make sure to install Flask: 
# https://flask.palletsprojects.com/en/2.0.x/installation/
# 
# The flow of this simulation is as follows:
# 1. Instantiates 3 different products
# 2. Instantiates 4 different wallets
# 3. Creates 10 different transactions between those 4 wallets,
#    using all 3 products
# 4. Mines transactions into blocks and blocks into the blockchain
# 5. 
# 
import blockchain as bch
import block as blk
import transaction as trn
import product as prd
import wallet as wlt
import miner as mnr

# Intantiating products
pr_claritin = prd.Product('claritin', 'merke')
pr_predinisone = prd.Product('predinisona', 'GSK')
pr_aspirin = prd.Product('aspirin','bayer')

print('These were the products created:')
print(pr_claritin, pr_predinisone, pr_aspirin)

# Instantiate our blockchain
bchain = bch.Blockchain()
for i in bchain.chain:
    print(i)
# Instantiating wallets
wl_manuf = wlt.Wallet(bchain)
wl_3pl = wlt.Wallet(bchain)
wl_dist = wlt.Wallet(bchain)
wl_dgstore = wlt.Wallet(bchain)

print('These wallets have these resources:')
print(wl_manuf, wl_3pl, wl_dist, wl_dgstore)

print('The following transactions occur:')

print("Manufacturer creates 100 units of aspirin")
bchain.transaction_broker('create', pr_aspirin, 100, wl_manuf, wl_manuf, "Batch production")

print("Manufacturer creats 150 units of predinisone")
bchain.transaction_broker('create', pr_predinisone, 150, wl_manuf, wl_manuf, "Batch production")

print("Manufacturer creates 200 units of claritin")
bchain.transaction_broker('create', pr_predinisone, 200, wl_manuf, wl_manuf, "Batch production")

print("Manufacturer handed off all products to the 3PL")
bchain.transaction_broker('transfer', pr_aspirin, 100, wl_manuf, wl_3pl, "Transfer for distribution")
bchain.transaction_broker('transfer', pr_predinisone, 150, wl_manuf, wl_3pl, "Transfer for distribution")
bchain.transaction_broker('transfer', pr_claritin, 200, wl_manuf, wl_3pl, "Transfer for distribution")

print("3PL delivers products to the distributor, losing 10 units of aspirin on the way")
bchain.transaction_broker('transfer', pr_aspirin, 90, wl_3pl, wl_dist, "Transfer for distribution")
bchain.transaction_broker('remove', pr_aspirin, 10, wl_3pl, wl_3pl,"Transfer for distribution")
bchain.transaction_broker('transfer', pr_predinisone, 150, wl_3pl, wl_dist, "Transfer for distribution")
bchain.transaction_broker('transfer', pr_claritin, 200, wl_3pl, wl_dist, "Transfer for distribution")

print("Distributor doses out the medication to pharmacies.. 30 units at a time")
bchain.transaction_broker('transfer', pr_aspirin, 30, wl_dist, wl_dgstore, "Transfer for distribution")
bchain.transaction_broker('transfer', pr_predinisone, 30, wl_dist, wl_dgstore, "Transfer for distribution")
bchain.transaction_broker('transfer', pr_claritin, 30, wl_dist, wl_dgstore, "Transfer for distribution")

print("This is the situation after all those transactions:")

## ADD MORE TRANSACTIONS

print(bchain.pool_transaction)

print("\nPeriodically, the miner inspects the chain looking for transactions to validate. It has found several and bundled it into different blocks (respecting the transaction limit per bloc):\n")

miner = mnr.Miner(bchain)
miner.bundle_pending_transactions()
miner.validate_block()
for i in bchain.pool_unconfirmed_block:
    bchain.add_block(i)
bchain.query_blocks()
