<template>
  <div class="home">
    <h1>Dashboard</h1>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->

    <div style="background: #ECECEC; padding: 60px">
      <a-row :gutter="64" type="flex" justify="start">
        <a-col :xs="{ span: 4, offset: 0 }" :lg="{ span: 8, offset: 0 }">
          <div>
            <v-chart :forceFit="true" :height="height" :data="data" :scale="scale">
              <v-tooltip />
              <v-axis />
              <v-legend />
              <v-line position="month*value" shape="hv" color="key" />
            </v-chart>
          </div>
          <br>
          <div>
            <v-chart :forceFit="true" :height="height" :data="data2" :scale="scale2">
              <v-tooltip :showTitle="false" dataKey="item*percent" />
              <v-axis />
              <v-legend dataKey="item" />
              <v-pie position="percent" color="item" :vStyle="pieStyle" :label="labelConfig" />
              <v-coord type="theta" :radius="0.75" :innerRadius="0.6" />
            </v-chart>
          </div>
        </a-col>
        <a-col :xs="{ span: 4, offset: 0 }" :lg="{ span: 8, offset: 0 }">
          <div>
            <v-chart :forceFit="true" :height="height" :data="data5" :scale="scale5">
              <v-tooltip />
              <v-axis />
              <v-legend />
              <v-line position="year*value" :size="2" color="country" adjust="stack" />
              <v-stack-area position="year*value" color="country" />
            </v-chart>
          </div>
          <br>
          <div>
            <v-chart :forceFit="true" :height="height" :data="expectData">
              <v-tooltip :showTitle="false" :itemTpl="tooltipOpts.itemTpl" />
              <v-coord type="rect" direction="LT" />
              <v-pyramid :position="pyramidOpts.position" :color="pyramidOpts.color"
                :label="pyramidOpts.label" :tooltip="pyramidOpts.tooltip" :opacity="pyramidOpts.opacity" />
              <v-view :data="actualData">
                <v-tooltip />
                <v-coord type="rect" direction="LT" />
                <v-pyramid :position="pyramidOpts1.position" :color="pyramidOpts1.color"
                  :vStyle="pyramidOpts1.style" :tooltip="pyramidOpts1.tooltip" :opacity="pyramidOpts1.opacity" />
              </v-view>
            </v-chart>
          </div>
        </a-col>
        <a-col :xs="{ span: 4, offset: 0.5 }" :lg="{ span: 6, offset: 1 }">
            <v-chart :forceFit="true" :height="height2" :data="data3">
              <v-tooltip />
              <v-axis />
              <v-legend />
              <v-stack-bar position="月份*月均降雨量" color="name" />
            </v-chart>
        </a-col>
      </a-row>                
    </div>
  </div>

</template>

<style scoped>
  .grid-Width {    
    background-color: rgb(163, 167, 166);
    border-radius: 4px;
    min-height: 100px;
  }
  .grid-a-Width {    
    background-color: rgb(81, 145, 131);
    border-radius: 4px;
    min-height: 220px;
  }
</style>

<script>
// graph1
const DataSet = require('@antv/data-set');
const sourceData = [
  { month: 'Jan', series2: 51, series1: 125 },
  { month: 'Feb', series2: 91, series1: 132 },
  { month: 'Mar', series2: 34, series1: 141 },
  { month: 'Apr', series2: 47, series1: 158 },
  { month: 'May', series2: 63, series1: 133 },
  { month: 'June', series2: 58, series1: 143 },
  { month: 'July', series2: 56, series1: 176 },
  { month: 'Aug', series2: 77, series1: 194 },
  { month: 'Sep', series2: 99, series1: 115 },
  { month: 'Oct', series2: 106, series1: 134 },
  { month: 'Nov', series2: 88, series1: 110 },
  { month: 'Dec', series2: 56, series1: 91 },
];

const dv = new DataSet.View().source(sourceData);
dv.transform({
  type: 'fold',
  fields: ['series1', 'series2'],
  key: 'key',
  value: 'value',
});
const data = dv.rows;

const scale = [{
  dataKey: 'month',
  min: 0,
  max: 1,
}];

// graph2
const sourceData2 = [
  { item: '1', count: 40 },
  { item: '2', count: 21 },
  { item: '3', count: 17 },
  { item: '4', count: 13 },
  { item: '5', count: 9 }
];

const scale2 = [{
  dataKey: 'percent',
  min: 0,
  formatter: '.0%',
}];

const dv2 = new DataSet.View().source(sourceData2);
dv2.transform({
  type: 'percent',
  field: 'count',
  dimension: 'item',
  as: 'percent'
});
const data2 = dv2.rows;

// graph 3
const sourceData3 = [
    { name: 'London', 'Jan.': 18.9, 'Feb.': 28.8, 'Mar.': 39.3, 'Apr.': 81.4, 'May': 47, 'Jun.': 20.3, 'Jul.': 24, 'Aug.': 35.6 },
    { name: 'Berlin', 'Jan.': 12.4, 'Feb.': 23.2, 'Mar.': 34.5, 'Apr.': 99.7, 'May': 52.6, 'Jun.': 35.5, 'Jul.': 37.4, 'Aug.': 42.4 },
  ];

  const dv3 = new DataSet.View().source(sourceData3);
  dv3.transform({
    type: 'fold',
    fields: ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.', 'Jul.', 'Aug.'],
    key: '月份',
    value: '月均降雨量',
  });
  const data3 = dv3.rows;

// graph 4
const expectData = [
  {value: 100, name: '展现'},
  {value: 80, name: '点击'},
  {value: 60, name: '访问'},
  {value: 40, name: '咨询'},
  {value: 30, name: '订单'},
];

const actualData = [
  {value: 80, name: '展现'},
  {value: 50, name: '点击'},
  {value: 30, name: '访问'},
  {value: 10, name: '咨询'},
  {value: 5, name: '订单'},
];

const tooltipOpts = {
  showTitle: false,
  itemTpl: '<li><span style="background-color:{color};" class="g2-tooltip-marker"></span>{name}: {value}</li>'
};

const pyramidOpts = {
  position: 'name*value',
  color: ['name', ['#0050B3', '#1890FF', '#40A9FF', '#69C0FF', '#BAE7FF']],
  label: ['name', {
    offset: 35,
    labelLine: {
      lineWidth: 1,
      stroke: 'rgba(0, 0, 0, 0.15)'
    }
  }],
  tooltip: ['name*value', (name, value) => {
    return {
      name: '预期' + name,
      value,
    };
  }],
  opacity: 0.65,
};

const pyramidOpts1 = {
  quickType: 'pyramid',
  position: 'name*value',
  color: ['name', [ '#0050B3', '#1890FF', '#40A9FF', '#69C0FF', '#BAE7FF' ]],
  tooltip: ['name*value', (name, value) => {
    return {
      name: '实际' + name,
      value,
    };
  }],
  style: {
    lineWidth: 1,
    stroke: '#fff',
  },
  opacity: 1,
};

// graph 5
  const data5 = [
    {country: 'Asia', year: '1750', value: 502},
    {country: 'Asia', year: '1800', value: 635},
    {country: 'Asia', year: '1850', value: 809},
    {country: 'Asia', year: '1900', value: 5268},
    {country: 'Asia', year: '1950', value: 4400},
    {country: 'Asia', year: '1999', value: 3634},
    {country: 'Asia', year: '2050', value: 947},
    {country: 'Africa', year: '1750', value: 106},
    {country: 'Africa', year: '1800', value: 107},
    {country: 'Africa', year: '1850', value: 111},
    {country: 'Africa', year: '1900', value: 1766},
    {country: 'Africa', year: '1950', value: 221},
    {country: 'Africa', year: '1999', value: 767},
    {country: 'Africa', year: '2050', value: 133},
    {country: 'Europe', year: '1750', value: 163},
    {country: 'Europe', year: '1800', value: 203},
    {country: 'Europe', year: '1850', value: 276},
    {country: 'Europe', year: '1900', value: 628},
    {country: 'Europe', year: '1950', value: 547},
    {country: 'Europe', year: '1999', value: 729},
    {country: 'Europe', year: '2050', value: 408},
    {country: 'Oceania', year: '1750', value: 200},
    {country: 'Oceania', year: '1800', value: 200},
    {country: 'Oceania', year: '1850', value: 200},
    {country: 'Oceania', year: '1900', value: 460},
    {country: 'Oceania', year: '1950', value: 230},
    {country: 'Oceania', year: '1999', value: 300},
    {country: 'Oceania', year: '2050', value: 300},
  ];

  const scale5 = [{
    dataKey: 'year',
    type: 'linear',
    tickInterval: 50,
  }];

export default {
  data() {
    return {
      data,
      data2,
      data3,
      data5,
      scale,
      scale2,
      scale5,
      expectData,
      actualData,
      height: 400,
      height2: 800,
      width: 350,
      tooltipOpts,
      pyramidOpts,
      pyramidOpts1,
      pieStyle: {
        stroke: "#fff",
        lineWidth: 1,
      },
      labelConfig: ['percent', {
        formatter: (val, item) => {
          return item.point.item + ': ' + val;
        }
      }],
    };
  }
};
</script>
