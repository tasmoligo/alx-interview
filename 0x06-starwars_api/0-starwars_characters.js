#!/usr/bin/node

const request = require('request');

const m_id = process.argv[1];
const m_endPoint = 'https://swapi-api.alx-tools/api/films/' + m_id;

function query (queryList, index) {
  if (queryList.length === index) {
    return;
  }

  request(queryList[index], (error, Response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      query(queryList, index + 1);
    }
  });

  request(m_endPoint, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const queryList = JSON.parse(body).characters;
      query(queryList, 0);
    }
  })
}
