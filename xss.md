Author: Mauricio I. Reyes Villanueva \

### Part I: Cookies

a. Yes, the cookie is for the domain: cs338.jeffondich.com.
The name is "theme" and the value is whatever theme is active, such as "default", "red", or "blue".

b. Yes, chaging the theme, changes the value of the cookie.

c. There is an initial GET request that is sent to the server requesting for the site, to which the server responds with a the standard headers, as well as a "Set-Cookie" header containing a value of "theme=default". From here the cookie is set, and later when we send other GET requests, they contain a "Cookie" header which has a value of "theme=default."

d. Yes. I selected the "blue" theme, and it was still there after relaunching my browser.

e. The current theme is transmitted between the browser and server via the "cookie" header in an http request which we initially include if we store the theme cookie in our browser, or is set if there is none via the server.

f. When we wish to change our theme we simply include the theme we want in the GET requests GET header params, as follows "GET /fdf/?theme=color HTTP/1.1". Additionally, the GET request also includes the current cookie via the "Cookie" header which contains a key value pair of "theme: color"

g. You can modify the theme's value field to the desired color.

h. You can modify the http GET request, using a proxy, before it's on route and change the cookie headers key value pair, "theme=color" to the desired "theme=color".

i. My OS (MacOS) stores chrome's cookies in the following directory: ~/Library/Application Support/Google/Chrome/Default/ in a file called "Cookies."

### Part II: Cross-Site Scripting (XSS)

a.

Moriarty breaks up his attack into two main parts, the "testing the waters phase", the "attack phase".

- First moriarty tests the waters by testing to see if injection of something "safe" like html w/ styling can be performed. 

- If he notices that this works, he goes on to try something more powerful such as javascript injection, to which he attacks other users.

- From here on, any user who opens up his posts will be "attacked" via the javascript injection.

b. A more virulent attack that Moriarty could have performed, would be something like writing javascript that redirects a user to a fake login page that may tell the user they were logged out and need to log back in, or even a page that modifies the contents of the site, to perform something malicious. Additionally, with javascript, you have access to the local/session/cookie storage found on jeffondich's site, this could contain information that you may not necessarily want shared, even if minor like website customizations.

c. Another attack that can possibly be performed, depending on how the site is configured, would be to perform javascript sql injections on the site which would be really dangerous and give the attacker various amounts of information they should not have access to.

d. Techniques that the server can use to prevent what Moriarty is doing is to parse user input, and remove any sort of code from posts. It could also take a more lenient approach and still parse the post, but only allow certain key tags such as markdown styling for it to be a "feature."

