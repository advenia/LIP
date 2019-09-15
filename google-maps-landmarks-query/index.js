const url = require('url');
const fs = require('fs');
const request = require('request');
const { Builder, By, Key, NoSuchElementError } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const cheerio = require('cheerio');


async function sleep(ms) {
    return new Promise((resolve) => {
        setTimeout(resolve, ms);
    });
}


const ADDRESS = '140 Westmount Rd N, Waterloo, Ontario, Canada';

(async () => {
    const driver = await new Builder()
          .forBrowser('chrome')
    // .setChromeOptions(new chrome.Options().addArguments(['--headless', '--windowsize=1920,1080']))
          .setChromeOptions(new chrome.Options().addArguments(['--no-proxy-server']))
          .build();
    try {
        await driver.get('https://www.google.com/maps/search/tourist+attractions/@43.4807955,-80.5540787,13z/data=!3m1!4b1');
        const locations = [];
        const getText = (o) => {
            console.log('o:', o);
            if(o === undefined) {
                return '';
            } else if(o.type === 'text') {
                // console.log('o.data:', o.data);
                return o.data;
            } else if(o.children !== undefined) {
                // console.log('o.children:', o.children);
                return o.children.map((e) => {return getText(e);}).join('');
            } else {
                return '';
            }
        };
        for(let i = 0; i < 9; i++) {
            const $ = cheerio.load(await driver.getPageSource());
            console.log($('h3'));
            ((a, b) => {
                a.map((e, i) => {
                    locations.push({                        
                        name: getText(a[e]).trim(),
                        address: getText(b[e]).trim()
                    });
                });
            })($('h3'), $('span.section-result-location'));
            break;
            await sleep(2000);
        }

        const out = [];
        for(let l in locations) {
            await driver.get(
                url.format({
                    protocol: 'https',
                    hostname: 'www.openstreetmap.org',
                    pathname: '/search',
                    query: {
                        query: locations[l].address + ', Waterloo, Ontario, Canada'
                    }
                })
            );
            const pair = url.parse(await driver.getCurrentUrl()).hash.split('/').slice(1);
            out.push({
                'name': locations[l].name,
                'address': locations[l].address,
                'latitude': pair[0],
                'longitude': pair[1]
            });
        }
        out.forEach((e) => {
            request.post({
                url: 'http://localhost:8000/polls/addpoint',
                form: e
            }, (err, res, body) => {
                console.log(body);
            });
        });
    } catch(e) {
        console.error(e);
    } finally {
        driver.quit();
    }
})();
