#!/usr/bin/node
const data = require('./100-data');

const initialList = data.list;
const newList = initialList.map((value, index) => value * index);

console.log('Initial List:', initialList);
console.log('New List:', newList);
