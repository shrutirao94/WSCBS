  var myService = {
      MyService: {
          MyPort: {
              Add: function(args) {
                  return args.x + args.y
              },
          }
      }
  };

  var xml = require('fs').readFileSync('myservice.wsdl', 'utf8');

  //http server example
  var server = http.createServer(function(request,response) {
      response.end('404: Not Found: ' + request.url);
  });

  server.listen(8000);
  soap.listen(server, '/wsdl', myService, xml);
