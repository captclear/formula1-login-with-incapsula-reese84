# formula1-login-with-incapsula-reese84
**Solve the problem of 403 when logging in to formula1, that is, the reese84 cookie is invalid**  

**Function**  
When simulating a request to log in to formula1, the status code 403 always appears. This is because there is a problem with the cookie we requested.  

**Testing**  
To solve this problem, we first need to find out which cookie is causing the problem. Finally, we find that it is the cookie reese84.

**Result**  
We generate reese84 cookie on api, and then bring it into the login request, then 403 will no longer be displayed, and the login will be normal.  

Therefore, when the response status code does not contain 403, it means that the generated reese84 cookie has taken effect.  
Response status code 200 Account and password are correct.  
Response status code 401 Account or password is incorrect.   
Response status code 422 InvalidProperty  

If you need my help, please DM me on tg. [@shineho](https://t.me/shineho)

**Debug Response**
![f1](https://github.com/captclear/formula1-login-with-incapsula-reese84/assets/173774216/61a2ebcd-bda4-4c5e-b9d0-53b41cefd1b6)


