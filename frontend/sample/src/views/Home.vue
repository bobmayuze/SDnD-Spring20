<template>
  <div class="home">
    <h1>Dashboard</h1>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->

    <div style="background: #fffff; padding: 60px">
      <a-row :gutter="64" type="flex" justify="start">
        <a-col :xs="{ span: 4, offset: 0 }" :lg="{ span: 6, offset: 0 }">
          <v-chart :forceFit="true" :height="650" :data="dataTop10">
            <v-coord type="rect" direction="LT" />
            <v-tooltip />
            <v-legend />
            <v-axis dataKey="value" position="right" />
            <v-axis dataKey="label" :label="labelTop10" />
            <v-bar position="label*value" color="type" />
          </v-chart>
        </a-col>
        <a-col :xs="{ span: 4, offset: 0 }" :lg="{ span: 8, offset: 0 }">
          <div>
            <v-chart :width="400" :height="300" :data="dataNum" :scale="scaleNum">
              <v-tooltip />
              <v-axis />
              <v-legend />
              <v-line position="year*value" :size="2" color="country" adjust="stack" />
              <v-stack-area position="year*value" color="country" />
            </v-chart>
          </div>
          <br>
            <div>
              <v-chart :width="400" :height="300" :data="dataPU" :scale="scalePU">
                <v-tooltip />
                <v-axis />
                <v-legend />
                <v-line position="month*temperature" color="city" />
                <v-point position="month*temperature" color="city" :size="4" :v-style="stylePU" :shape="'circle'" />
              </v-chart>
            </div>
        </a-col>
        <a-col :xs="{ span: 4, offset: 0 }" :lg="{ span: 8, offset: 0 }">
          <div>
            <v-chart :width="400" :height="300" :data="dataPU" :scale="scalePU">
              <v-tooltip />
              <v-axis />
              <v-legend />
              <v-line position="month*temperature" color="city" />
              <v-point position="month*temperature" color="city" :size="4" :v-style="stylePU" :shape="'circle'" />
            </v-chart>
          </div>
          <br>
          <div>
            <v-chart :width="400" :height="300" :data="data7" :scale="scale7">
              <v-tooltip :showTitle="false" dataKey="item*percent" />
              <v-axis />
              <v-legend dataKey="item" />
              <v-pie position="percent" color="item" :vStyle="pieStyle7" :label="labelConfig7" />
              <v-coord type="theta" :radius="0.75" :innerRadius="0.6" />
            </v-chart>
          </div>
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
  const DataSet = require('@antv/data-set');
// top 10
  const sourceDataTop10 = [
    { label: 'A', PV: 974, UV: 132 },
    { label: 'B', PV: 877, UV: 106 },
    { label: 'C', PV: 789, UV: 84 },
    { label: 'D', PV: 710, UV: 68 },
    { label: 'E', PV: 639, UV: 54 },
    { label: 'F', PV: 575, UV: 43 },
    { label: 'G', PV: 518, UV: 35 },
    { label: 'H', PV: 466, UV: 28 },
    { label: 'I', PV: 419, UV: 22 },
    { label: 'J', PV: 377, UV: 18 },
  ];

  const dvTop10 = new DataSet.View().source(sourceDataTop10);
  dvTop10.transform({
    type: 'fold',
    fields: ['PV', 'UV'],
    key: 'type',
    value: 'value',
  });
  const dataTop10 = dvTop10.rows;
  const labelTop10 = { offset: 12 };

  // # templates
  const dataNum = [
      {country: 'Medical', year: '1750', value: 502},
      {country: 'Medical', year: '1800', value: 635},
      {country: 'Medical', year: '1850', value: 809},
      {country: 'Medical', year: '1900', value: 5268},
      {country: 'Medical', year: '1950', value: 4400},
      {country: 'Medical', year: '1999', value: 3634},
      {country: 'Medical', year: '2050', value: 947},
      {country: 'Retail', year: '1750', value: 106},
      {country: 'Retail', year: '1800', value: 107},
      {country: 'Retail', year: '1850', value: 111},
      {country: 'Retail', year: '1900', value: 1766},
      {country: 'Retail', year: '1950', value: 221},
      {country: 'Retail', year: '1999', value: 767},
      {country: 'Retail', year: '2050', value: 133},
      {country: 'Finance', year: '1750', value: 163},
      {country: 'Finance', year: '1800', value: 203},
      {country: 'Finance', year: '1850', value: 276},
      {country: 'Finance', year: '1900', value: 628},
      {country: 'Finance', year: '1950', value: 547},
      {country: 'Finance', year: '1999', value: 729},
      {country: 'Finance', year: '2050', value: 408},
    ];

  const scaleNum = [{
    dataKey: 'year',
    type: 'linear',
    tickInterval: 50,
  }];

  // PV & UV
  const sourceDataPU = [
  { month: 'Jan', Tokyo: 7.0, London: 3.9 },
  { month: 'Feb', Tokyo: 6.9, London: 4.2 },
  { month: 'Mar', Tokyo: 9.5, London: 5.7 },
  { month: 'Apr', Tokyo: 14.5, London: 8.5 },
  { month: 'May', Tokyo: 18.4, London: 11.9 },
  { month: 'Jun', Tokyo: 21.5, London: 15.2 },
  { month: 'Jul', Tokyo: 25.2, London: 17.0 },
  { month: 'Aug', Tokyo: 26.5, London: 16.6 },
  { month: 'Sep', Tokyo: 23.3, London: 14.2 },
  { month: 'Oct', Tokyo: 18.3, London: 10.3 },
  { month: 'Nov', Tokyo: 13.9, London: 6.6 },
  { month: 'Dec', Tokyo: 9.6, London: 4.8 },
];

const dvPU = new DataSet.View().source(sourceDataPU);
dvPU.transform({
  type: 'fold',
  fields: ['Tokyo', 'London'],
  key: 'city',
  value: 'temperature',
});
const dataPU = dvPU.rows;

const scalePU = [{
  dataKey: 'month',
  min: 0,
  max: 1,
}];

// last 7 days
const sourceData7 = [
  { item: 'Medical', count: 40 },
  { item: 'Retail', count: 21 },
  { item: 'Finance', count: 17 },
  { item: 'Manufacture', count: 13 },
];

const scale7 = [{
  dataKey: 'percent',
  min: 0,
  formatter: '.0%',
}];

const dv7 = new DataSet.View().source(sourceData7);
dv7.transform({
  type: 'percent',
  field: 'count',
  dimension: 'item',
  as: 'percent'
});
const data7 = dv7.rows;

  export default {
    data() {
      return {
        dataTop10,
        heightTop10: 800,
        label: labelTop10,
        dataNum,
        scaleNum,
        heightNum: 400,
        dataPU,
        scalePU,
        heightPU: 400,
        stylePU: { stroke: '#fff', lineWidth: 1 },
        data7,
        scale7,
        height7: 400,
        pieStyle7: {
          stroke: "#fff",
          lineWidth: 1,
        },
        labelConfig7: ['percent', {
          formatter: (val, item) => {
            return item.point.item + ': ' + val;
          }
        }],
      };
    }
  };
</script>
