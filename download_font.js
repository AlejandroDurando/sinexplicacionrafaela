const puppeteer = require('puppeteer');
const fs = require('fs');
const https = require('https');

(async () => {
    try {
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36');
        
        console.log("Navigating to wfonts.com...");
        await page.goto('https://www.wfonts.com/download/data/2016/04/23/big-noodle-titling/bignoodletitling.zip', {waitUntil: 'networkidle2'});
        const buffer = await page.evaluate(() => {
            return new Promise(resolve => {
                fetch('https://www.wfonts.com/download/data/2016/04/23/big-noodle-titling/bignoodletitling.zip')
                  .then(r => r.arrayBuffer())
                  .then(ab => Array.from(new Uint8Array(ab)))
                  .then(resolve);
            });
        });
        
        fs.writeFileSync('bnt.zip', Buffer.from(buffer));
        console.log('Saved to bnt.zip');
        await browser.close();
    } catch (e) {
        console.error("Error:", e);
        process.exit(1);
    }
})();
