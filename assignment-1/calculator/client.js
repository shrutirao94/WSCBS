var soap = require('soap');
var url = 'http://localhost:8080/spec?wsdl';
// var args = { "x": "4", "y": "6" };
var args = { x: "7.5", y: "0" };

soap.createClient(url, function(err, client) {
  client.Add(args, function(err, res) {
    console.log(res.result);
  })

  client.Sub(args, function(err, res) {
    console.log(res.result);
  })

  client.Mul(args, function(err, res) {
    console.log(res.result);
  })

  client.Div(args, function(err, res) {
    console.log(res.result);
  })
});
