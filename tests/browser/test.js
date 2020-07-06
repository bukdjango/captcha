const puppeteer = require('puppeteer');


(async () => {
  const browser = await puppeteer.launch({
    args: [
        '--no-sandbox',
        '--headless',
        '--disable-gpu',
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
    ]
  });
  await new Promise(resolve => setTimeout(resolve, 2000));
  const page = await browser.newPage();
  // await page.setExtraHTTPHeaders({'Host': 'bukdjango_captcha.com'})
  await page.goto('http://captcha/recaptcha_v3/', {waitUntil: 'networkidle0'});
  await new Promise(resolve => setTimeout(resolve, 1000));
  await page.click('input[type=submit]')
  await page.screenshot({path: 'example.png'});

  console.log(await page.content())
    await browser.close();
})();