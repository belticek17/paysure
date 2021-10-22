##  Hiring project

The goal  of this assignment is to assess candidates skills as well as dive slightly into solving problems that occur during our day to day work. The idea is to start by implementing the first rule, then try add the remaining rules. Invest one to two hours into trying to solve the assignment and see where you can get.


## Task
Implement payment server `handle` method so that it responds in xml whether the payment  should be accepted or  declined. The format example is in `src/resources/response.xml`.

Decision whether to accept payments should be done based on following rules:

1. Sufficient money is present on account (InsufficientFunds)
2. One accepted transaction allowed per day per card (TransactionCountOverLimit)
3. Single transaction limit is 150 eur (TransactionAmountOverLimit)
4. Decline all transactions if it is raining at merchant location (ItsRaining)
5. If it's less than  10 °C the transaction limit is only 50 %
6. If it's sunny allow up to two transactions per day from those locations
7. If the wind is blowing from North to South charge account of the bank instead of customer

Transaction data should be saved (file saving is sufficient)

We strongly suggest you to use the following library in your implementation as it should simplify the process:
https://orinoco.readthedocs.io/en/latest/

You can use pre-defined action for weather information.

Payments in example should do the following if send in order they are numbered:

1. accept
2. decline InsufficientFunds
3. decline TransactionAmountOverLimit
4. decline TransactionCountOverLimit
5. accept
6. accept
7. accept
8. decline TransactionAmountOverLimit
9. accept
10. accept
11. decline  ItsRaining
12. decline  ItsRaining
13. decline  InsufficientFunds
14. decline  ItsRaining
15. decline
16. decline InsufficientFunds
17. accept
18. accept
19. decline TransactionCountOverLimit
20. decline TransactionCountOverLimit 


Remaining amounts on account should be following:

card - `1234567890` - 190 EUR 

card - `0987654321` - 20 EUR

Bank - 999 800 EUR
