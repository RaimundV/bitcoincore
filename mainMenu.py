import bitcoinCore

while True:
    print ("1. transaction tax")
    print ("2. Block changed")
    choice = raw_input("choose an item: ")

    bitcoinCore.transactionOrBlock(choice)

    if choice != "1" and choice != "2":
        break




