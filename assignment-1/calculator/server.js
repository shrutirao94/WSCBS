var http = require('http');
var soap = require('soap');

var myService = {
  CalculatorService: {
    CalculatorPort: {
      Add: function(args) {
        return { result: `The sum is: ${parseFloat(args.x) + parseFloat(args.y)}` }
      },
      Sub: function(args) {
        return { result: `The difference is: ${parseFloat(args.x) - parseFloat(args.y)}`}
      },
      Mul: function(args) {
        return { result: `The product is: ${parseFloat(args.x) * parseFloat(args.y)}`}
      },
      Div: function(args) {
        return { result: `The quotient is: ${parseFloat(args.x) / parseFloat(args.y)}`}
      }
    }
  }
};

var xml = require('fs').readFileSync('spec.wsdl', 'utf8');
var server = http.createServer(function(req, res) {
  res.end('404: Not Found' + req.url);
});

server.listen(8080);
soap.listen(server, '/spec', myService, xml);
