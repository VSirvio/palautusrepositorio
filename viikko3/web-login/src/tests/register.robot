*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  woeufhjdknj
    Set Password  hewuf7refhjfe
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ty
    Set Password  ehflwe7wefreiet
    Submit Credentials
    Registration Should Fail With Message  Username should be at least 3 characters long

Register With Valid Username And Invalid Password
    Set Username  iwjudfdndsn
    Set Password  ifnlsfesndLll
    Submit Credentials
    Registration Should Fail With Message  Password should also contain other characters than a-z and A-Z

Register With Nonmatching Password And Password Confirmation
    Set Username  nslefllilhe
    Input Password  password  salasana1
    Input Password  password_confirmation  salosana1
    Submit Credentials
    Registration Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  ueworhuewb
    Set Password  euw5ukeffsldifl
    Submit Credentials
    Logout
    Set Username  ueworhuewb
    Input Password  password  euw5ukeffsldifl
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  nu
    Set Password  sfehu4ncuew
    Submit Credentials
    Click Link  Login
    Set Username  nu
    Input Password  password  sfehu4ncuew
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Logout
    Click Link  Continue to main page
    Click Button  Logout

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password}

Registration Should Succeed
    Page Should Contain  Welcome to Ohtu Application!

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
