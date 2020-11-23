The traditional way to store sessions is with session ID cookies. After you login to a website, a session object is created for you on the backend (the server), and your browser (the client) is given a cookie which identifies that object. As you make requests to the site, your browser automatically sends the session ID cookie to the backend server, which uses that ID to find your session in its own memory and thus authorise you to perform actions.

JWTs work differently. After you login, the server sends your web browser the whole session object in a JWT, containing a payload of key-value pairs describing your username, privileges, and other info. Also included is a signature created using the server's secret key, designed to prevent you from tampering with the payload. Your web browser saves the token into local storage.

On subsequent requests, your browser sends the token to the backend server. The server verifies the signature first, and then reads the token payload to authorise you.

To summarise, with session ID cookies, sessions live on the server, but with JWTs, sessions live on the client.

The main advantage of JWTs over session ID cookies is that they are easy to scale. Organisations need a way to share sessions across multiple backend servers. When a client switches from using one server or resource to another, that client's session should still work. Furthermore, for large orgs there could be millions of sessions. Since JWTs live on the client, they solve these problems: any backend server can authorise a user just by checking the signature on the token and reading the data inside.

Unfortunately there are some downsides to JWTs, as they are often configured in an insecure way, and clients are free to modify them and see if the server will still verify them. We'll look at these exploits in the next challenges. For now, the flag is the name of the HTTP header used by the browser to send JWTs to the server. 