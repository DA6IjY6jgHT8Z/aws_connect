# A portfolio sample AWS Connect Instance

## Components

### DynamoDB tables
- holidays
  - (date, description)
- caller_id
  - (caller_phone, sales_rep)

### Lambda functions - (called from Connect)
- holiday_query 
  - { "holiday": "Christmas" }
  - { "holiday": "None" }
- get_caller_id_lambda 
  - { "sales_rep": "1234" }

### Lex bot
- MainMenu

### Connect Contact Flow
- car_main

### Connect Queues
- Sales
- Service
- Financing


## Summary
This is an example car dealer contact center. I am utilizing the `holiday_query` lambda to query the `holidays` lambda which returns a holiday name if there is one, otherwise `"None"`.

#### Holiday
If it does have a holiday the following happens:
 - "Thank you for calling the Car Dealer. We are closed for the $.Attributes.['cHoliday'] holiday. Please call back on the next business day."
 - call is disconnected

#### Business Hours
If it found no holiday:
 - It checks for the regular business hours assigned in Connect
   - If it is not durring business hours:
     - "Thank you for calling the Car Dealer. We are closed. Please call back during our regular business hours."

#### Main Menu
If it is not a holiday and it is durring business hours it will continue to the MainMenu bot.
- "Thank you for calling the Car Dealer.  What are you calling about?  Press 1 for sales, 2 for service and 3 for financing."
  - for service and financing it gets sent to the respective queues
  - for sales the `get_caller_id_lambda` is called to identify if the phone number the caller is calling from has a sales rep assigned to them
    - if not, they are sent to the `Sales` queue
    - if they do have a sales rep the rep criteria would then be defined to route to that rep (currently not setup) 


## Issues
Provisioning a number for Connect
- "We couldn't claim your phone number - Phone number not available: +17015783673. Try again with a different available number"
- "We couldn't claim your phone number - The allowed limit for claimed phone numbers has been exceeded for your instance"

## Further Development
- I would need to assign sales reps and get the routing criteria assigned to them
- Further defining bot utterances
- I'm working on getting everything into a CDK stack but only have a basic lambda built so far.
- setup finance self-service options
- setup service self-service options

