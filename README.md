# Time Clock Automation Script
### Skip all the clickinggggg....

## Dependencies
### Selenium 
`pip3 install selenium`

## Commands
### To initialize your secrets.yaml file, run:
`./clock.sh init`
#### Note: The URL must contain the numerical identifier at the beginning and the end:
`https://281685.tcplusondemand.com/app/webclock/#/EmployeeLogOn/281685`

### To test, run:
`./clock.sh test`

### To clock in, run:
`./clock.sh in`

### To clock out, run:
`./clock.sh out`

### To start meal period, run:
`./clock.sh hungry`

### To end meal period, run:
`./clock.sh full`