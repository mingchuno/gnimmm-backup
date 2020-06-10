const fs = require('fs')
const es = require('event-stream')

let count = 0
const s = fs.createReadStream('gnimmm.jl')
    .pipe(es.split())
    .pipe(es.map(function (data, cb) {
      const item = JSON.parse(data)
      const fileData = `${item.title}\n\n${item.text}\n\n${item.url}`
      fs.writeFile(`output/${item.datetime.substring(0,10)}-${item.title}.txt`, fileData, (err) => {
        if (err) cb(err)
        count++
        console.log(`The file has been saved![${count}]`)
        cb()
      })
    }))
    .on('error', function(err){
        console.log('Error while reading file.', err);
    })
    .on('end', function(){
        console.log('Read entire file.')
    })
