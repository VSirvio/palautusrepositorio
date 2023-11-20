*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  cat  abcd3fgh
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  jokunimi  salasana15
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  re  ssdfh7dfs
    Output Should Contain  Username should be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  uwjffdl6sfe  ygy3skhuflsdi8
    Output Should Contain  Username should consist only of lowercase letters a-z

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  huskhflsdil  ef7sdij
    Output Should Contain  Password should be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  idsfihiwfc  sduhKsdj
    Output Should Contain  Password should also contain other characters than a-z and A-Z

*** Keywords **
Input New Command And Create User
    Input New Command
    Input Credentials  jokunimi  huonosalasana2
