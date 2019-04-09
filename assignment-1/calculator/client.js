const  soap = require('soap');
const url = 'http://localhost:8080/spec?wsdl';
const args = { command: process.argv[2], x: process.argv [3], y: process.argv[4] } 

soap.createClient(url, function(err, client) {
  switch (args.command) {
    default:
      console.log("No command found! Please specify add, sub, mul or div!")
      break;

    case "add":
      client.Add(args, function(err, res) { 
        console.log(res.result); 
      })
      break;

    case "sub":
      client.Sub(args, function(err, res) {
        console.log(res.result); 
      })
      break;

    case "mul":
      client.Mul(args, function(err, res) {
        console.log(res.result); 
      })
      break;
    
    case "div":
      client.Div(args, function(err, res) { 
        console.log(res.result); 
      })
      break;
  }
});
