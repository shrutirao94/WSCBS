var soap = require('soap')
var url = 'http://127.0.0.1./wsdl?wsdl'
var args = {x: 2, y: 1}
soap.createClient(url, function(err, client) {
    client.Add(args, function(err, result) {
        console.log(result)
    })
})
