var express = require('express')
  , partials = require('express-partials')
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
	app.use(partials())
	partials.register('.mustache', mustache)
	app.use(app.router);
	app.use(express.static(__dirname + '/static'));
});

app.get('/', function(req, res){
	var replays = fs.readdirSync(REPLAY_OUTPUT_FOLDER);
	res.render("replayList", {replays: replays})
});

function getFileJson(matchId, filename) {
	//security? what is this security you are talking about? arbitrary path traversal? Is it bad?
	//should be fixed by the regex that grabs the id...
	var data = fs.readFileSync(REPLAY_OUTPUT_FOLDER+"/"+matchId+"/"+ filename +".json",encoding="utf8");
	if ( data instanceof Error ) {
		console.log("Could not get file '"+filename+"'")
		return []
  }

	console.log("Got file '"+filename+"'")
	return [JSON.parse(data)]
}

app.get('/details/:id([a-zA-Z0-9]+$)', function(req, res){
	var replayId = req.params.id

	var summaryData = getFileJson(replayId, "summary")
	var factionConflictData = getFileJson(replayId, "factionConflict")

	res.render("details", {summary: summaryData,factionConflict: factionConflictData})
});

app.listen(PORT);
console.log('Listening on port '+PORT);
