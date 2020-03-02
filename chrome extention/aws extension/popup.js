document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('button')[0].addEventListener('click', onclick, false)
  document.querySelectorAll("button")[1].addEventListener("click", seeStats, false);
  
  function onclick () {
    chrome.tabs.query({currentWindow: true, active: true}, function (tabs) {
      chrome.tabs.sendMessage(tabs[0].id, 'hi', setCount)
    })
  }
  function seeStats() {
    chrome.tabs.query({currentWindow: true, active: true}, function (tabs) {
        chrome.tabs.create({url: "stats.html"});
      })
  }
  function setCount (res) {
    const div = document.createElement('div')
    // div.textContent = `${res.isFraud} `
    // document.body.appendChild(div)
  }
}, false)