from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

PORT = 8080

currency_rates = {
    'USD': 1.0, 'EUR': 0.85, 'CAD': 1.25, 'GBP': 0.75, 'INR': 83.2,
    'AUD': 1.49, 'JPY': 140.9, 'CNY': 7.15, 'CHF': 0.91, 'NZD': 1.62,
    'SGD': 1.35, 'ZAR': 18.5, 'AED': 3.67, 'BRL': 4.92, 'MXN': 16.9,
    'RUB': 92.5, 'SEK': 10.2, 'NOK': 10.5, 'HKD': 7.84, 'KRW': 1305.0
}

currency_metadata = {
    'USD': 'United States', 'EUR': 'Eurozone', 'CAD': 'Canada',
    'GBP': 'United Kingdom', 'INR': 'India', 'AUD': 'Australia',
    'JPY': 'Japan', 'CNY': 'China', 'CHF': 'Switzerland',
    'NZD': 'New Zealand', 'SGD': 'Singapore', 'ZAR': 'South Africa',
    'AED': 'UAE', 'BRL': 'Brazil', 'MXN': 'Mexico', 'RUB': 'Russia',
    'SEK': 'Sweden', 'NOK': 'Norway', 'HKD': 'Hong Kong',
    'KRW': 'South Korea'
}

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == 'index.html':
            try:
                with open('index.html', 'r', encoding='utf-8') as f:
                    html = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, 'index.html not found')

        elif self.path == '/style.css':
            try:
                with open('style.css', 'r', encoding='utf-8') as f:
                    css = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                self.wfile.write(css.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, 'style.css not found')

        elif self.path == '/h.html':
            try:
                with open('h.html', 'r', encoding='utf-8') as f:
                    html = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, 'h.html not found')


        
        elif self.path == '/h.css':
            try:
                with open('h.css', 'r', encoding='utf-8') as f:
                    css = f.read()
                    self.send_response(200)
                    self.send_header('Content-type', 'text/css')
                    self.end_headers()
                    self.wfile.write(css.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, 'h.css not found')



        elif self.path == '/h.js':
            try:
                with open('h.js', 'r', encoding='utf-8') as f:
                    js = f.read()
                    self.send_response(200)
                    self.send_header('Content-type', 'application/javascript')
                    self.end_headers()
                    self.wfile.write(js.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, 'h.js not found')




        else:
            self.send_error(404, 'File not found')
        

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = urllib.parse.parse_qs(post_data.decode())

        try:
            amount = float(data['amount'][0])
            source = data['source_currency'][0]
            target = data['target_currency'][0]

            if source == target:
                converted = amount
            else:
                usd_amount = amount / currency_rates[source]
                converted = usd_amount * currency_rates[target]

            source_country = currency_metadata.get(source, 'Unknown')
            target_country = currency_metadata.get(target, 'Unknown')

            result = f"<h3>{amount} {source} ({source_country}) = {converted:.2f} {target} ({target_country})</h3>"
        except:
            result = "<h3 style='color:red;'>Invalid input.</h3>"

        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()

        html = html.replace("<!--RESULT-->", result)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('localhost', PORT), MyHandler)
    print(f"Server running on http://localhost:{PORT}")
    server.serve_forever()
