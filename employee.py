"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from enum import Enum

class Employee:
    def __init__(self, name):
        self.name = name
        contract = ContractType.UNKNOWN

        #amountPerTime, commission, hours, commissionLength = None

    def __str__(self):
        pay = self.name + " works on a"
        totalPayString = ".  Their total pay is "
        commissionString = " and receives a "
        if (self.contract == ContractType.MONTHLY):
            pay += " monthly salary of " + str(self.amountPerTime)
        elif (self.contract == ContractType.HOURLY):
            pay += " contract of " + str(self.hours) + " hours at " + str(self.amountPerTime) + "/hour"
        else:
            return name + " has no contract at the moment"

        totalPay = 0

        if (self.commission != None):
            totalPay = self.commission
            if (self.commissionLength != None):
                pay += commissionString + "commission for " + str(self.commissionLength) + " contract(s) at " + str(self.commission) + "/contract"
                totalPay *= self.commissionLength
            else:
                pay += commissionString + "bonus commission of " + str(self.commission)

        pay += totalPayString + str(self.get_pay()) + "."

        return pay

    def set_contract(self, contract, amountPerTime, hours, commission, commissionLength): #if the contract is monthly
        self.contract = contract
        self.amountPerTime = amountPerTime
        self.hours = hours
        self.commission = commission
        self.commissionLength = commissionLength

    def get_pay(self):
        totalPay = 0

        if (self.commission != None):
            totalPay = self.commission
            if (self.commissionLength != None):
                totalPay *= self.commissionLength

        if (self.hours != None):
            totalPay += self.amountPerTime * self.hours
        else:
            totalPay += self.amountPerTime

        return totalPay

class ContractType(Enum):
    UNKNOWN = 0
    MONTHLY = 1
    HOURLY = 2

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.set_contract(ContractType.MONTHLY, 4000, None, None, None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.set_contract(ContractType.HOURLY, 25, 100, None, None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.set_contract(ContractType.MONTHLY, 3000, None, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.set_contract(ContractType.HOURLY, 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.set_contract(ContractType.MONTHLY, 2000, None, 1500, None)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.set_contract(ContractType.HOURLY, 30, 120, 600, None)

if (True):
    assert billie.get_pay() == 4000
    string = 'Billie works on a monthly salary of 4000.  Their total pay is 4000.'
    assert str(billie) == string

    assert charlie.get_pay() == 2500
    string = 'Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.'
    assert str(charlie) == string

    assert renee.get_pay() == 3800
    string = 'Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.'
    assert str(renee) == string

    assert jan.get_pay() == 4410
    string  = 'Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.'
    assert str(jan) == string

    assert robbie.get_pay() == 3500
    string = 'Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.'
    assert str(robbie) == string

    assert ariel.get_pay() == 4200
    string = 'Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.'
    assert str(ariel) == string
