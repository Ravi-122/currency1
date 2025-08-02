const histories = {
  USD: { symbol: "$", formed: "1792", issuedBy: "Federal Reserve", developedBy: "U.S. Congress" },
  EUR: { symbol: "€", formed: "1999", issuedBy: "European Central Bank", developedBy: "European Union" },
  CAD: { symbol: "C$", formed: "1858", issuedBy: "Bank of Canada", developedBy: "Govt. of Canada" },
  GBP: { symbol: "£", formed: "8th Century", issuedBy: "Bank of England", developedBy: "Anglo-Saxon England" },
  INR: { symbol: "₹", formed: "1947", issuedBy: "Reserve Bank of India", developedBy: "Govt. of India" },
  AUD: { symbol: "A$", formed: "1966", issuedBy: "Reserve Bank of Australia", developedBy: "Govt. of Australia" },
  JPY: { symbol: "¥", formed: "1871", issuedBy: "Bank of Japan", developedBy: "Meiji Government" },
  CNY: { symbol: "¥", formed: "1948", issuedBy: "People's Bank of China", developedBy: "People’s Republic of China" },
  CHF: { symbol: "CHF", formed: "1850", issuedBy: "Swiss National Bank", developedBy: "Swiss Confederation" },
  NZD: { symbol: "NZ$", formed: "1967", issuedBy: "Reserve Bank of New Zealand", developedBy: "Govt. of New Zealand" },
  SGD: { symbol: "S$", formed: "1967", issuedBy: "Monetary Authority of Singapore", developedBy: "Govt. of Singapore" },
  ZAR: { symbol: "R", formed: "1961", issuedBy: "South African Reserve Bank", developedBy: "Govt. of South Africa" },
  AED: { symbol: "د.إ", formed: "1973", issuedBy: "Central Bank of UAE", developedBy: "UAE Government" },
  BRL: { symbol: "R$", formed: "1994", issuedBy: "Central Bank of Brazil", developedBy: "Govt. of Brazil" },
  MXN: { symbol: "$", formed: "1823", issuedBy: "Bank of Mexico", developedBy: "Mexican Government" },
  RUB: { symbol: "₽", formed: "1991", issuedBy: "Central Bank of Russia", developedBy: "Russian Federation" },
  SEK: { symbol: "kr", formed: "1873", issuedBy: "Sveriges Riksbank", developedBy: "Govt. of Sweden" },
  NOK: { symbol: "kr", formed: "1875", issuedBy: "Norges Bank", developedBy: "Govt. of Norway" },
  HKD: { symbol: "HK$", formed: "1935", issuedBy: "Hong Kong Monetary Authority", developedBy: "Govt. of Hong Kong" },
  KRW: { symbol: "₩", formed: "1945", issuedBy: "Bank of Korea", developedBy: "South Korean Govt." }
};

function showHistory() {
  const select = document.getElementById("currency-select");
  const infoDiv = document.getElementById("currency-info");
  const currency = histories[select.value];

  if (currency) {
    infoDiv.innerHTML = `
      <div class="card">
        <h2>${select.options[select.selectedIndex].text}</h2>
        <p><strong>Symbol:</strong> ${currency.symbol}</p>
        <p><strong>Formed:</strong> ${currency.formed}</p>
        <p><strong>Issued By:</strong> ${currency.issuedBy}</p>
        <p><strong>Developed By:</strong> ${currency.developedBy}</p>
      </div>
    `;
    infoDiv.style.display = "block";
  } else {
    infoDiv.innerHTML = "";
    infoDiv.style.display = "none";
  }
}
