var express = require('express')
  , fs = require('fs')
  , mustache = require('mustache')
	, cons = require('consolidate')
var app = express()

var PORT = 9000
var REPLAY_OUTPUT_FOLDER = "../data/output/"

app.configure(function() {
	app.engine("mustache",cons.mustache) //assign mustache to .mustache files
	app.set('view engine', 'mustache');
	app.set('views', __dirname + '/views');
	app.use(app.router);
	app.use(express.static(__dirname + '/static'));
});

app.get('/', function(req, res){
	var replays = fs.readdirSync(REPLAY_OUTPUT_FOLDER);
	res.render("replayList", {replays: replays})
});

app.get('/summary/:id([a-zA-Z0-9]+$)', function(req, res){
	//security? what is this security you are talking about? arbitrary path traversal? Is it bad?
	//should be fixed by the regex
	var summaryData = fs.readFileSync(REPLAY_OUTPUT_FOLDER+"/"+req.params.id+"/"+"summary.json",encoding="utf8");
	summaryData = JSON.parse(summaryData)
	res.render("matchSummary", summaryData)
});

app.listen(PORT);
console.log('Listening on port '+PORT);
