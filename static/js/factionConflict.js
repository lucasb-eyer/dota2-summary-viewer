nv.addGraph(function() {
  var chart = nv.models.stackedAreaChart()
                .x(function(d) { return d.time })
                .y(function(d) { return 1 })
                .clipEdge(true);

  chart.xAxis
      .showMaxMin(false)
      .tickFormat(function(d) { return d3.time.format('%x')(new Date(d)) });

  chart.yAxis
      .tickFormat(d3.format(',.2f'));

  d3.select('#chardDeatchsAll svg')
    .datum(data.events)
      .transition().duration(500).call(chart);

  nv.utils.windowResize(chart.update);

  return chart;
});

