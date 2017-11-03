const axios = require('axios');

function getBit() {
    return axios('https://api.bitfinex.com/v1/pubticker/btcusd')
        .then((response) => {
            return response;
        })
        .catch((err) => {
            console.error(err);
        });
}

module.exports = {
    getBit
};