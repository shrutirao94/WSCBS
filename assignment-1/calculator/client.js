const  soap = require('soap');
const url = 'http://localhost:8080/spec?wsdl';
const args = { x: process.argv [2], y: process.argv[3] }

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
