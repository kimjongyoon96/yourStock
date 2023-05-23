const http = require("http");

http
  .createServer((request, response) => {
    response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    return response.end("<p>listening on port 8000</p>");
  })
  .listen(8000, () => {
    console.log("listening on port 8000");
  });
