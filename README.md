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


**Debug Response**
![f1](https://github.com/captclear/formula1-login-with-incapsula-reese84/assets/173774216/61a2ebcd-bda4-4c5e-b9d0-53b41cefd1b6)


---

### ⚠️ Important Notice:
Please ensure that any actions you take comply with [Spotify's Terms of Service](https://www.spotify.com/legal/end-user-agreement/) and [GitHub's Community Guidelines](https://docs.github.com/en/github/site-policy/github-community-guidelines). Unauthorized or abusive practices may result in the suspension of your accounts on these platforms. Always use tools and scripts responsibly and within the bounds of the law.

### Disclaimer
This guide and the accompanying information are provided for educational and informational purposes only. **They are not intended for commercial use**. The author does not endorse or support any use of this information that may violate the terms and conditions of Formula1, GitHub, or any other platform mentioned.

By using this guide, you acknowledge that:
- You are solely responsible for how you choose to use the information provided.
- Any actions taken based on this guide are done at your own risk.
- The author is not liable for any direct or indirect damages, including but not limited to account suspension, legal consequences, or any other issues arising from the use of this information.
- You agree to comply with all applicable laws and regulations in your jurisdiction. Any legal repercussions resulting from the use or misuse of this information are solely your responsibility, and the author assumes no liability.

This guide is intended to foster learning and understanding. It should not be used to engage in any illegal or unethical activities. If you have any doubts or concerns, please consult with legal professionals or refer to the terms and conditions of the respective platforms before proceeding.

coding need my help, pls dm me on tg. [@shineho](https://t.me/shineho).

